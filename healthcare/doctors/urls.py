from .views import *
from django.urls import path

urlpatterns = [
    path('get-all-doctors/',all_doctors_view),
    path('get_doctor_slots/',get_doctor_slots),
    path('book_appointment/',book_appointment),
 
]