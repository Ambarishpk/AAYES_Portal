from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aayesapp.urls')),
    # Add other URL patterns as needed
]
