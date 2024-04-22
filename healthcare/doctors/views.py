from django.http import JsonResponse
from .models import DoctorProfile
from healthcare.helper.responses import success_response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_doctors_view(request):
    name = request.GET.get('name')
    gender = request.GET.get('gender')

    doctors_queryset = DoctorProfile.objects.all()

    if name:
        doctors_queryset = doctors_queryset.filter(user__user_name__icontains=name)

    if gender:
        doctors_queryset = doctors_queryset.filter(user__gender=gender)

    doctor_data = []
    for doctor in doctors_queryset:
        doctor_data.append({
            'username': doctor.user.user_name,
            'gender':doctor.user.gender,
            'personal_profile': doctor.personal_profile,
            'rating': doctor.rating,
            'years_of_experience': doctor.years_of_experience,
            'price': str(doctor.price) if doctor.price else None,
            'specializations': [specialization.specialization for specialization in doctor.specialization.all()],
            'personal_experiences': [{'title': experience.title, 'description': experience.description} for experience in doctor.personalexperience_set.all()],
            'availability': [{'date': availability.date, 'start_time': availability.start_time, 'end_time': availability.end_time} for availability in doctor.doctoravaliability_set.all()]
        })

    return JsonResponse(success_response(message="Doctors Shown successfully", data=doctor_data), status=status.HTTP_200_OK)

