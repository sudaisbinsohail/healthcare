from django.http import JsonResponse
from .models import DoctorProfile , AvailabilitySlots
from healthcare.helper.responses import success_response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from datetime import timedelta , datetime


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_doctors_view(request):
    name = request.GET.get('name')
    gender = request.GET.get('gender')
    specialization = request.GET.get('specialization')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort_by_price = request.GET.get('sort_by_price')

    doctors_queryset = DoctorProfile.objects.all()

    if name:
        doctors_queryset = doctors_queryset.filter(user__user_name__icontains=name)

    if gender:
        doctors_queryset = doctors_queryset.filter(user__gender=gender)

    if specialization:
        doctors_queryset = doctors_queryset.filter(specialization__specialization__icontains=specialization)

    if min_price is not None:
        doctors_queryset = doctors_queryset.filter(price__gte=min_price)

    if max_price is not None:
        doctors_queryset = doctors_queryset.filter(price__lte=max_price)

    if sort_by_price == 'asc':
        doctors_queryset = doctors_queryset.order_by('price')
    elif sort_by_price == 'desc':
        doctors_queryset = doctors_queryset.order_by('-price')

    doctor_data = []
    for doctor in doctors_queryset:
        doctor_data.append({
            'id':doctor.id,
            'username': doctor.user.user_name,
            'gender':doctor.user.gender,
            'personal_profile': doctor.personal_profile,
            'rating': doctor.rating,
            'years_of_experience': doctor.years_of_experience,
            'price': str(doctor.price) if doctor.price else None,
            'specializations': [specialization.specialization for specialization in doctor.specialization.all()],
            'personal_experiences': [{'title': experience.title, 'description': experience.description} for experience in doctor.personalexperience_set.all()],
        })

    return JsonResponse(success_response(message="Doctors Shown successfully", data=doctor_data), status=status.HTTP_200_OK)






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctor_slots(request):
    id = request.GET.get('doctor_id')
    if id:
        try:
            doctor_profile = DoctorProfile.objects.get(id = id)
        except Exception as e :
            return Response({"message":"Sorry user Does Not exist"},status=status.HTTP_400_BAD_REQUEST)
    
    slots = AvailabilitySlots.objects.filter(doctor_id=doctor_profile.id)
    serializedSlots = AvailabilitySlotsSerializer(slots , many=True)
    available_slots_by_day = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': [],
            'Sunday': []
        }

    for slot in slots:
            start_time = slot.start_time
            end_time = slot.end_time
            break_start_time = slot.break_start_time
            break_end_time = slot.break_end_time
            slot_duration = slot.slot_duration
            day_of_week = slot.day_of_week

            current_time = datetime.combine(datetime.today(), start_time)
            end_datetime = datetime.combine(datetime.today(), end_time)
            break_start_datetime = datetime.combine(datetime.today(), break_start_time)
            break_end_datetime = datetime.combine(datetime.today(), break_end_time)

            while current_time < end_datetime:
                if break_start_datetime <= current_time < break_end_datetime:
                    current_time = break_end_datetime
                    continue

                end_slot_time = min(current_time + slot_duration, end_datetime)
                available_slots_by_day[day_of_week].append({
                    'start_time': current_time.time(),
                    'end_time': end_slot_time.time()
                })

                current_time += slot_duration

    return JsonResponse(success_response(message="Doctors Avaliability Timings successfully", data=available_slots_by_day), status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_appointment(request):
    try:
        serializer = BookAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            error_details = serializer.errors.get('non_field_errors', [])
            error_codes = [error.code for error in error_details]
            if(error_codes[0] == 'unique'):
                return Response({"status":"Fail","message":"An appointment already exists for this doctor at this time."}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 