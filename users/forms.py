from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, SupervisorAssignment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'ep_number', 
                 'company_name', 'plant', 'department', 'trade', 'skill', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class BulkUserUploadForm(forms.Form):
    csv_file = forms.FileField(
        widget=forms.FileInput(attrs={'accept': '.csv', 'class': 'form-control'})
    )

class SupervisorAssignmentForm(forms.ModelForm):
    class Meta:
        model = SupervisorAssignment
        fields = ['supervisor', 'employee', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.role == 'user1':
            self.fields['supervisor'].queryset = User.objects.filter(role='user2', company_name=user.company_name)
            self.fields['employee'].queryset = User.objects.filter(role='user3', company_name=user.company_name)