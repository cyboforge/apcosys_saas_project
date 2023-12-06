from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from employee.models import Employee
from .forms import  UserAuthenticationForm, EmployeeEditForm

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



def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    
    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/admin/dashboard')
    else:
        form = EmployeeEditForm(instance=employee)
    
    return render(request, 'custom_admin/edit_employee.html', {'form': form, 'employee': employee})
