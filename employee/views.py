from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserAuthenticationForm
from .models import Employee
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout

def employee_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email
            user = Employee.objects.create(username=username, email=email, first_name=first_name, last_name=last_name, password=make_password(password))
            user.set_password(password)
            return redirect('/employee/login')
    else:
        form = UserRegistrationForm()
    return render(request, 'employee/registration.html', {'form': form})

def employee_login(request):
    if request.method == 'POST':
        
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request=request,username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/employee/dashboard')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = UserAuthenticationForm()
    return render(request, 'employee/login.html', {'form': form})

def employee_logout(request):
    logout(request)
    return redirect('/employee/login')
    

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'employee/dashboard.html')
    return redirect('/employee/login')