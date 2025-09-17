from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SupervisorAssignment, AuditLog, Notification

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'role', 'ep_number', 'company_name', 'is_active']
    list_filter = ['role', 'company_name', 'is_active']
    search_fields = ['username', 'email', 'ep_number', 'first_name', 'last_name']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('role', 'ep_number', 'company_name', 'plant', 'department', 'trade', 'skill', 'start_date', 'end_date', 'force_password_change')
        }),
    )

@admin.register(SupervisorAssignment)
class SupervisorAssignmentAdmin(admin.ModelAdmin):
    list_display = ['supervisor', 'employee', 'start_date', 'end_date', 'assigned_by']
    list_filter = ['start_date', 'end_date']
    search_fields = ['supervisor__username', 'employee__username']

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'model_name', 'timestamp']
    list_filter = ['action', 'model_name', 'timestamp']
    search_fields = ['user__username', 'model_name']
    readonly_fields = ['user', 'action', 'model_name', 'object_id', 'old_value', 'new_value', 'timestamp']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['user__username', 'title']