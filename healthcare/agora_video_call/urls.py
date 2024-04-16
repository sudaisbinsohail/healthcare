from .views import *
from django.urls import path

urlpatterns = [
    path('initate-call/',generate_agora_token),
 
]