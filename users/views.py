import csv
import io
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import User, SupervisorAssignment, AuditLog, Notification
from .forms import CustomUserCreationForm, CustomLoginForm, BulkUserUploadForm, SupervisorAssignmentForm
from .utils import cleanup_orphaned_user3_accounts
from attendance.models import AttendanceRecord

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    context = {'user': user}
    
    if user.role == 'master':
        context.update({
            'total_companies': User.objects.filter(role='user1').values('company_name').distinct().count(),
            'total_users': User.objects.count(),
            'recent_uploads': AttendanceRecord.objects.select_related('user').order_by('-created_at')[:10]
        })
    elif user.role == 'user1':
        context.update({
            'company_employees': User.objects.filter(company_name=user.company_name, role='user3').count(),
            'company_supervisors': User.objects.filter(company_name=user.company_name, role='user2').count(),
            'recent_attendance': AttendanceRecord.objects.filter(user__company_name=user.company_name).order_by('-date')[:10]
        })
    elif user.role == 'user2':
        assigned_employees = SupervisorAssignment.objects.filter(supervisor=user).values_list('employee', flat=True)
        context.update({
            'assigned_employees': User.objects.filter(id__in=assigned_employees),
            'recent_attendance': AttendanceRecord.objects.filter(user__id__in=assigned_employees).order_by('-date')[:10]
        })
    elif user.role == 'user3':
        attendance_summary = AttendanceRecord.objects.filter(user=user).values('status').annotate(count=Count('status'))
        context['attendance_summary'] = {item['status']: item['count'] for item in attendance_summary}
    
    return render(request, 'users/dashboard.html', context)

@login_required
def create_user(request):
    if request.user.role not in ['master', 'user1']:
        messages.error(request, 'Permission denied.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if request.user.role == 'user1':
                user.company_name = request.user.company_name
            user.save()
            messages.success(request, f'User {user.username} created successfully.')
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/create_user.html', {'form': form})

@login_required
def bulk_user_upload(request):
    if request.user.role not in ['master', 'user1']:
        messages.error(request, 'Permission denied.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = BulkUserUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)
            
            created_count = 0
            error_count = 0
            errors = []
            
            for row_num, row in enumerate(reader, start=2):
                try:
                    username = row.get('Username') or row.get('EP Number')
                    password = row.get('Password') or row.get('EP Number')
                    
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=row.get('Email', ''),
                        first_name=row.get('Name', '').split()[0] if row.get('Name') else '',
                        last_name=' '.join(row.get('Name', '').split()[1:]) if row.get('Name') else '',
                        role=row.get('Role', 'user3').lower(),
                        ep_number=row.get('EP Number'),
                        company_name=row.get('Company Name'),
                        plant=row.get('Plant'),
                        department=row.get('Department'),
                        trade=row.get('Trade'),
                        skill=row.get('Skill')
                    )
                    created_count += 1
                except Exception as e:
                    error_count += 1
                    errors.append(f"Row {row_num}: {str(e)}")
            
            # Provide detailed feedback
            if error_count == 0:
                # All users created successfully
                messages.success(request, f'✅ Data Successfully Updated! Created {created_count} user accounts.')
            elif created_count > 0:
                # Partial success
                messages.success(request, f'✅ Partially Updated! Created {created_count} user accounts successfully.')
                messages.warning(request, f'⚠️ {error_count} users could not be created due to errors.')
                # Show first 5 errors
                for error in errors[:5]:
                    messages.error(request, error)
                if len(errors) > 5:
                    messages.error(request, f'... and {len(errors) - 5} more errors.')
            else:
                # Complete failure
                messages.error(request, f'❌ Data Not Updated! All {error_count} users failed to create.')
                # Show first 10 errors
                for error in errors[:10]:
                    messages.error(request, error)
                if len(errors) > 10:
                    messages.error(request, f'... and {len(errors) - 10} more errors.')
            
            return redirect('bulk_user_upload')
    else:
        form = BulkUserUploadForm()
    
    return render(request, 'users/bulk_upload.html', {'form': form})

@login_required
def user_list(request):
    if request.user.role == 'master':
        users = User.objects.all()
    elif request.user.role == 'user1':
        users = User.objects.filter(company_name=request.user.company_name)
    else:
        messages.error(request, 'Permission denied.')
        return redirect('dashboard')
    
    search = request.GET.get('search')
    if search:
        users = users.filter(
            Q(username__icontains=search) | 
            Q(first_name__icontains=search) | 
            Q(last_name__icontains=search) | 
            Q(ep_number__icontains=search)
        )
    
    paginator = Paginator(users, 25)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    
    return render(request, 'users/user_list.html', {'users': users})

@login_required
def delete_company_data(request):
    if request.user.role != 'master':
        messages.error(request, 'Permission denied.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        delete_blank = request.POST.get('delete_blank')
        
        if company_name:
            # Delete attendance records first
            attendance_count = AttendanceRecord.objects.filter(user__company_name=company_name).count()
            AttendanceRecord.objects.filter(user__company_name=company_name).delete()
            
            # Delete all users for the company (this includes all roles)
            user_count = User.objects.filter(company_name=company_name).count()
            User.objects.filter(company_name=company_name).delete()
            
            messages.success(request, f'Deleted {user_count} users and {attendance_count} attendance records for company: {company_name}')
        elif delete_blank:
            # Delete attendance records with blank/null company names
            attendance_count = AttendanceRecord.objects.filter(Q(user__company_name__isnull=True) | Q(user__company_name='')).count()
            AttendanceRecord.objects.filter(Q(user__company_name__isnull=True) | Q(user__company_name='')).delete()
            
            # Delete users with blank company names
            user_count = User.objects.filter(Q(company_name__isnull=True) | Q(company_name='')).count()
            User.objects.filter(Q(company_name__isnull=True) | Q(company_name='')).delete()
            
            messages.success(request, f'Deleted {user_count} users and {attendance_count} attendance records with blank company names')
        else:
            messages.error(request, 'Please select a company or choose to delete blank records.')
    
    companies = User.objects.values_list('company_name', flat=True).distinct().exclude(company_name__isnull=True).exclude(company_name='')
    blank_count = User.objects.filter(Q(company_name__isnull=True) | Q(company_name='')).count()
    return render(request, 'users/delete_company.html', {'companies': companies, 'blank_count': blank_count})

@login_required
def download_user_template(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users_template.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Role', 'EP Number', 'Name', 'Company Name', 'Username', 'Password', 'Email', 'Start Date', 'End Date', 'Plant', 'Department', 'Trade', 'Skill'])
    writer.writerow(['user1', 'ADMIN001', 'Admin User', 'ABC Company', 'admin001', 'admin123', 'admin@abc.com', '2024-01-01', '', 'Plant 1', 'Administration', '', ''])
    writer.writerow(['user2', 'SUP001', 'Supervisor One', 'ABC Company', 'sup001', 'sup123', 'sup1@abc.com', '2024-01-01', '', 'Plant 1', 'Production', 'Supervisor', ''])
    writer.writerow(['user3', 'EMP001', 'Employee One', 'ABC Company', '', '', 'emp1@abc.com', '2024-01-01', '', 'Plant 1', 'Production', 'Welder', 'Skilled'])
    
    return response

@login_required
def delete_attendance_data(request):
    if request.user.role != 'master':
        messages.error(request, 'Permission denied.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        if start_date and end_date:
            from attendance.models import AttendanceRecord
            
            # Delete attendance records
            deleted_count = AttendanceRecord.objects.filter(date__gte=start_date, date__lte=end_date).count()
            AttendanceRecord.objects.filter(date__gte=start_date, date__lte=end_date).delete()
            
            # Clean up orphaned User3 accounts
            deleted_users_count, deleted_usernames = cleanup_orphaned_user3_accounts()
            
            message = f'Deleted {deleted_count} attendance records from {start_date} to {end_date}'
            if deleted_users_count > 0:
                message += f' and removed {deleted_users_count} User3 accounts with no remaining attendance: {", ".join(deleted_usernames)}'
            
            messages.success(request, message)
        else:
            messages.error(request, 'Both start date and end date are required.')
    
    return render(request, 'users/delete_attendance.html')

@login_required
def notifications(request):
    user_notifications = request.user.notifications.all()
    paginator = Paginator(user_notifications, 20)
    page = request.GET.get('page')
    notifications = paginator.get_page(page)
    
    # Mark as read
    request.user.notifications.filter(is_read=False).update(is_read=True)
    
    return render(request, 'users/notifications.html', {'notifications': notifications})