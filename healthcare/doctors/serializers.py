from rest_framework import serializers
from .models import *
from django.db import IntegrityError
from datetime import datetime , timedelta , date


class AvailabilitySlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlots
        fields = '__all__'



class BookAppointmentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Appointment
        fields = '__all__'

     def validate(self, attrs):
        doctor_profile_id = attrs.get("doctor")
        appointment_start_time = attrs.get("start_time")
        appointment_end_time = attrs.get("end_time")
        appointment_date = attrs.get("appointment_date")


        if attrs.get('start_time') >= attrs.get('end_time'):
            raise serializers.ValidationError("End time must be after start time.")


        availability_slots = AvailabilitySlots.objects.filter(
            doctor_id=doctor_profile_id,
            day_of_week=appointment_date.strftime('%A')
        ).first()

        if availability_slots:
            avaliablity_start_datetime = datetime.combine(datetime.today(), availability_slots.start_time)
            avaliablity_end_datetime = datetime.combine(datetime.today(), availability_slots.end_time)
            avaliablity_break_start_datetime = datetime.combine(datetime.today(), availability_slots.break_start_time)
            avaliablity_break_end_datetime = datetime.combine(datetime.today(), availability_slots.break_end_time)
            slot_duration_minutes = availability_slots.slot_duration.seconds // 60
            slots = []
            current_datetime = avaliablity_start_datetime
            while current_datetime < avaliablity_end_datetime:
                if (
                    avaliablity_break_start_datetime <= current_datetime <= avaliablity_break_end_datetime
                    or avaliablity_break_start_datetime <= (current_datetime + timedelta(minutes=slot_duration_minutes)) <= avaliablity_break_end_datetime
                ):
                    current_datetime += timedelta(minutes=slot_duration_minutes)
                    continue
                slots.append({
                    'start_time': current_datetime.time(),
                    'end_time': (current_datetime + timedelta(minutes=slot_duration_minutes)).time()
                })

                current_datetime += timedelta(minutes=slot_duration_minutes)


        for slot in slots:
            if (
                slot['start_time'] <= appointment_start_time <= slot['end_time']
                and slot['start_time'] < appointment_end_time <= slot['end_time']
            ):
                return attrs
       
        raise serializers.ValidationError("Appointment time is not within available slots.")


      
       
     def create(self , validated_data):
         return Appointment.objects.create(**validated_data)
       