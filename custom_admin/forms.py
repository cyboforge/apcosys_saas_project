from django import forms
from employee.models import Employee

class UserAuthenticationForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    required = ['email','password']

class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'is_active']
