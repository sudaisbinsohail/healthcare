from rest_framework import serializers
from .models import *

class AvailabilitySlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlots
        fields = '__all__'