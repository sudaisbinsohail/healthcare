from .views import *
from django.urls import path

urlpatterns = [
    path('get-all-patient/',get_all_patient)
]
