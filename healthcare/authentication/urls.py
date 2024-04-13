from .views import *
from django.urls import path

urlpatterns = [
    path('register-user/', register),
    path('login-user/',login),
    path('refresh-token/',refreshToken),
    path('me/',getLoginUser)
]
