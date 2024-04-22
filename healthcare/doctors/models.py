from django.db import models
from healthcare.server import settings

class Specialization(models.Model):
    specialization = models.CharField(unique=True , max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    personal_profile = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(default=0)
    years_of_experience = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True , blank=True)
    specialization = models.ManyToManyField(Specialization, related_name='doctor_profile', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PersonalExperience(models.Model):
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DoctorAvaliability(models.Model):
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



