from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Allergy(models.Model):
    allergy = models.CharField(unique=True , max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MedicalCondition(models.Model):
    medical_conditions = models.CharField(unique=True , max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SpecificMedication(models.Model):
    specific_medication = models.CharField(unique=True , max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HealthProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=255)
    medical_history = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0)
    fitness_level = models.PositiveIntegerField(default=0)
    alcohol_use= models.IntegerField(default=0)
    sleep_in_hours = models.IntegerField(default=0)
    mood = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, null=True , blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True , blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2 , null=True , blank=True)
    allergies = models.ManyToManyField(Allergy, related_name='health_profiles', blank=True)
    medical_condition = models.ManyToManyField(MedicalCondition, related_name='health_profiles', blank=True)
    specific_medication = models.ManyToManyField(SpecificMedication, related_name='health_profiles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


