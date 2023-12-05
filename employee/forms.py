from django import forms
from .models import Employee

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['first_name','last_name','email','password']
        required = ['first_name','last_name','email','password']
        

class UserAuthenticationForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    required = ['email','password']
