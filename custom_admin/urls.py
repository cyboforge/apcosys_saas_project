from django.urls import include, path

from .views import dashboard, admin_login, admin_logout

urlpatterns = [
    path('login',admin_login, name = 'admin_login'),
    path('dashboard', dashboard, name = 'admin_dashboard'),
    path('logout', admin_logout, name = 'admin_logout'),
]