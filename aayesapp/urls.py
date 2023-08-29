from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registration, name='registration'),
    path('application-status/', views.status_check, name='application-status'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('apply-for-volunteer/', views.registration, name='apply-for-volunteer'),
    path('events/', views.events, name='events'),
    path('modules/', views.modules, name='modules'),
    path('pending-applications/', views.approval, name='pending-applications'),
    path('approve/', views.approval, name='approve'),
    # Add other URL patterns as needed
]
