from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from employee.models import Employee
from .forms import  UserAuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout


def admin_login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request=request,username=email, password=password)
            if user is not None and user.is_superuser == True:
                login(request, user)
                return redirect('/admin/dashboard')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = UserAuthenticationForm()
    return render(request, 'custom_admin/login.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('/admin/login')
    

def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        employee_list = Employee.objects.filter()
        return render(request, 'custom_admin/dashboard.html',{
            'employee_list': employee_list
        })
    return redirect('/admin/login')