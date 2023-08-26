from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registration, name='registration'),
    # Add other URL patterns as needed
]
