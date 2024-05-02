from django.db import models
from healthcare.server import settings
from django.core.exceptions import ValidationError
from datetime import timedelta
from healthcare.healthprofile.models import *

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
    is_avaliable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def clean(self):
        if DoctorAvaliability.objects.filter(doctor=self.doctor).exclude(id=self.id).exists():
            raise ValidationError('Doctor availability already exists.')

class AvailabilitySlots(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_start_time = models.TimeField()
    break_end_time = models.TimeField()
    slot_duration = models.DurationField(default=timedelta(hours=1))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        #  start_time is before end_time
        if self.start_time >= self.end_time:
            raise ValidationError(('Start time must be before end time.'))

        #  break_start_time is before break_end_time
        if self.break_start_time >= self.break_end_time:
            raise ValidationError(('Break start time must be before break end time.'))

        # break time falls within the availability window
        if not (self.start_time <= self.break_start_time <= self.break_end_time <= self.end_time):
            raise ValidationError(('Break time must fall within the availability window.'))

        #  only one AvailabilitySlots record exists per day of the week per doctor
        if AvailabilitySlots.objects.filter(doctor=self.doctor, day_of_week=self.day_of_week).exclude(id=self.id).exists():
            raise ValidationError(('Availability slots already exist for this day of the week.'))

    class Meta:
        unique_together = ('doctor', 'day_of_week')



class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Booked', ('Booked')),
        ('Cancelled', ('Cancelled')),
        ('Done', ('Done')),
    )

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(HealthProfile, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Booked')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Appointment')
        verbose_name_plural = ('Appointments')
        unique_together = ('doctor', 'appointment_date', 'start_time')

    def clean(self):
        # end time is after start time
        if self.start_time >= self.end_time:
            raise ValidationError(_('Start time must be before end time.'))







