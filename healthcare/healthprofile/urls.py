from .views import *
from django.urls import path

urlpatterns = [
    path('create-health-profile/',create_health_profile)
]