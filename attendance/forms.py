from django import forms
from .models import AttendanceRecord

class AttendanceUploadForm(forms.Form):
    csv_file = forms.FileField(
        widget=forms.FileInput(attrs={'accept': '.csv', 'class': 'form-control'})
    )

class AttendanceEditForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['in1', 'out1', 'in2', 'out2', 'in3', 'out3', 'hours_worked', 'overtime', 'status', 'supervisor_remarks', 'employee_remarks']
        widgets = {
            'in1': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'out1': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'in2': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'out2': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'in3': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'out3': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hours_worked': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'overtime': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'supervisor_remarks': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'employee_remarks': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class AttendanceFilterForm(forms.Form):
    STATUS_CHOICES = [('', 'All Status')] + AttendanceRecord.STATUS_CHOICES
    
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    employee = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Employee name or EP number', 'class': 'form-control'}))