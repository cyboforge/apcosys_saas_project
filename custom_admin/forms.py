from django import forms

class UserAuthenticationForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    required = ['email','password']

