from .views import *
from django.urls import path

urlpatterns = [
    path('create-health-profile/',create_health_profile),
    path('get-allergies/',get_allergies),
    path('get-medical-condition/',get_medical_condition),
    path('get-specific-medication/',get_specific_medication),
    path('get-user-health-profile/',get_health_profile)
]