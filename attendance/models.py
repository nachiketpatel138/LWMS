from django.db import models
from users.models import User

class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('-0.5', 'Half Day'),
        ('-1', 'Full Day Deduction'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    shift = models.CharField(max_length=50, null=True, blank=True)
    in1 = models.TimeField(null=True, blank=True)
    out1 = models.TimeField(null=True, blank=True)
    in2 = models.TimeField(null=True, blank=True)
    out2 = models.TimeField(null=True, blank=True)
    in3 = models.TimeField(null=True, blank=True)
    out3 = models.TimeField(null=True, blank=True)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    overtime = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='P')
    supervisor_remarks = models.TextField(null=True, blank=True)
    employee_remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']
    
    def get_hours_formatted(self):
        """Convert decimal hours to HH:MM format"""
        if not self.hours_worked:
            return "00:00"
        
        total_minutes = int(self.hours_worked * 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours:02d}:{minutes:02d}"
    
    def get_overtime_formatted(self):
        """Convert decimal overtime to HH:MM format"""
        if not self.overtime:
            return "00:00"
        
        total_minutes = int(self.overtime * 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours:02d}:{minutes:02d}"
    
    def __str__(self):
        return f"{self.user.username} - {self.date} ({self.status})"

class UploadHistory(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    total_rows = models.IntegerField()
    accepted_rows = models.IntegerField()
    rejected_rows = models.IntegerField()
    error_file = models.FileField(upload_to='upload_errors/', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.filename} - {self.upload_date}"