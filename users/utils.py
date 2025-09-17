from .models import User
from attendance.models import AttendanceRecord

def cleanup_orphaned_user3_accounts():
    """
    Remove User3 (Employee) accounts that have no attendance records.
    Returns count of deleted users and their usernames.
    """
    # Find User3 accounts that have no attendance records
    users_with_attendance = AttendanceRecord.objects.values_list('user_id', flat=True).distinct()
    
    orphaned_users = User.objects.filter(
        role='user3'
    ).exclude(
        id__in=users_with_attendance
    )
    
    deleted_count = orphaned_users.count()
    deleted_usernames = list(orphaned_users.values_list('username', flat=True))
    
    # Delete orphaned User3 accounts
    orphaned_users.delete()
    
    return deleted_count, deleted_usernames

def cleanup_user3_by_ep_numbers(ep_numbers_to_keep):
    """
    Remove User3 accounts whose EP numbers are not in the provided list.
    Used when uploading new attendance data to clean up old employees.
    """
    if not ep_numbers_to_keep:
        return 0, []
    
    users_to_delete = User.objects.filter(
        role='user3'
    ).exclude(
        ep_number__in=ep_numbers_to_keep
    )
    
    deleted_count = users_to_delete.count()
    deleted_usernames = list(users_to_delete.values_list('username', flat=True))
    
    users_to_delete.delete()
    
    return deleted_count, deleted_usernames