from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_health_profile(request):
    if request.method == 'POST':
        user = request.user 
        request.data['user'] = user.id 
        serializer = HealthProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_allergies(request):
            allergies = Allergy.objects.all()
            allergies = AllergySerializer(allergies,many=True)
            return Response(allergies.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_medical_condition(request):
            medical_condition = MedicalCondition.objects.all()
            medical_condition = MedicalConditionSerializer(medical_condition,many=True)
            return Response(medical_condition.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_specific_medication(request):
            specific_medication = SpecificMedication.objects.all()
            specific_medication = SpecificMedicationSerializer(specific_medication,many=True)
            return Response(specific_medication.data, status=status.HTTP_200_OK)
       



