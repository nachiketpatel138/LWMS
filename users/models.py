from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('master', 'Master User'),
        ('user1', 'User1 (Company Admin)'),
        ('user2', 'User2 (Supervisor)'),
        ('user3', 'User3 (Employee)'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user3')
    ep_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    plant = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    trade = models.CharField(max_length=100, null=True, blank=True)
    skill = models.CharField(max_length=100, null=True, blank=True)
    shift = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    force_password_change = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class SupervisorAssignment(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervised_employees')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervisors')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments_made')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['supervisor', 'employee', 'start_date']

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('restore', 'Restore'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} {self.action} {self.model_name} at {self.timestamp}"

class NotificationManager(models.Manager):
    def unread(self):
        return self.filter(is_read=False)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = NotificationManager()
    
    class Meta:
        ordering = ['-created_at']