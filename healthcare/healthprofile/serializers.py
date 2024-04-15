
from rest_framework import serializers
from .models import HealthProfile, Allergy , MedicalCondition , SpecificMedication

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'


class MedicalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCondition
        fields = '__all__'


class SpecificMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificMedication
        fields = '__all__'

class HealthProfileSerializer(serializers.ModelSerializer):
    allergies = serializers.PrimaryKeyRelatedField(many=True, queryset=Allergy.objects.all())
    medical_condition = serializers.PrimaryKeyRelatedField(many=True, queryset=MedicalCondition.objects.all())
    specific_medication = serializers.PrimaryKeyRelatedField(many=True, queryset=SpecificMedication.objects.all())

    class Meta:
        model = HealthProfile
        fields = '__all__'

    def create(self, validated_data):
        allergies_data = validated_data.pop('allergies')
        medication_condition = validated_data.pop('medical_condition')
        specific_medication = validated_data.pop('specific_medication')
        health_profile = HealthProfile.objects.create(**validated_data)
        health_profile.allergies.set(allergies_data)
        health_profile.medical_condition.set(medication_condition)
        health_profile.specific_medication.set(specific_medication)
        return health_profile
    
