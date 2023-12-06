from django.urls import include, path

from .views import dashboard, admin_login, admin_logout, edit_employee

urlpatterns = [
    path('login',admin_login, name = 'admin_login'),
    path('dashboard', dashboard, name = 'admin_dashboard'),
    path('logout', admin_logout, name = 'admin_logout'),
    path('edit_employee/<int:employee_id>', edit_employee, name='edit_employee'),

]