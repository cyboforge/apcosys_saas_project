from django.urls import include, path

from employee.views import dashboard, employee_login, employee_logout, employee_registration

urlpatterns = [
    path('login',employee_login, name = 'employee_login'),
    path('signup', employee_registration, name = 'employee_registeration'),
    path('dashboard', dashboard, name = 'dashboard'),
    path('logout', employee_logout, name = 'employee_logout'),
]