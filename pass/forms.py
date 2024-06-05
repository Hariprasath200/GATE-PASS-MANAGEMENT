from datetime import datetime
from django import forms
from .models import *
from datetime import time


class StdForm(forms.ModelForm):
    class Meta:
        model = Std
        fields = ['student_name', 'reg_no', 'email', 'mobile_number', 'description', 'parent_name', 'parent_number', 'department']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_number': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }

class HodStatusForm(forms.ModelForm):
    class Meta:
        model = Std
        fields = ['hod_status']


from django import forms
from datetime import time

class TimeRangeField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (
            forms.TimeField(),
            forms.TimeField(),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            start_time, end_time = data_list
            return f"{start_time} to {end_time}"
        return ""

class QRCodeForm(forms.Form):
    student_name = forms.CharField(label='Student Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    reg_no = forms.CharField(label='Registration Number', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='Status', choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], initial='PENDING', widget=forms.Select(attrs={'class': 'form-control'}))
    current_time = datetime.now()
    out_time = forms.DateTimeField(label='Out Time', initial=current_time, widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}))
    in_time = forms.DateTimeField(label='In Time', initial=current_time, widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}))




# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=UserProfile.USER_ROLES)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    role = forms.ChoiceField(choices=UserProfile.USER_ROLES)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
