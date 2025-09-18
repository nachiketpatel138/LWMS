from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from users.models import User
from attendance.models import AttendanceRecord

@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user:
        return Response({
            'success': True,
            'user': {
                'id': user.id,
                'username': user.username,
                'role': user.role,
                'company_name': user.company_name
            }
        })
    return Response({'success': False, 'error': 'Invalid credentials'})

@api_view(['GET'])
def dashboard_api(request):
    # Return dashboard data as JSON
    return Response({
        'total_users': User.objects.count(),
        'total_attendance': AttendanceRecord.objects.count()
    })