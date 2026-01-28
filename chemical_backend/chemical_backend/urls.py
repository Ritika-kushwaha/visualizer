from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line connects your main project to the api/urls.py you shared
    path('', include('api.urls')), 
]