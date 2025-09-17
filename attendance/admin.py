from django.contrib import admin
from .models import AttendanceRecord, UploadHistory

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'status', 'hours_worked', 'overtime', 'created_at']
    list_filter = ['status', 'date', 'user__company_name']
    search_fields = ['user__username', 'user__ep_number', 'user__first_name', 'user__last_name']
    date_hierarchy = 'date'

@admin.register(UploadHistory)
class UploadHistoryAdmin(admin.ModelAdmin):
    list_display = ['filename', 'uploaded_by', 'total_rows', 'accepted_rows', 'rejected_rows', 'upload_date']
    list_filter = ['upload_date', 'uploaded_by']
    search_fields = ['filename', 'uploaded_by__username']