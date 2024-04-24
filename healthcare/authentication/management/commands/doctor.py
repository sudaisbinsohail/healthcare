from django.core.management.base import BaseCommand
from healthcare.authentication.models import User
from healthcare.doctors.models import Specialization, DoctorProfile, PersonalExperience, DoctorAvaliability , AvailabilitySlots
from datetime import date, time


   

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **options):

        
       
        # create_specializations()
        # create_doctor_profiles()
        # create_personal_experiences()
        # create_doctor_availabilities()
        doctor_avaliable_slots()
        print('Sample data seeded successfully.')

        self.stdout.write(self.style.SUCCESS('Database seeding complete'))
def create_specializations():
            Specialization.objects.create(specialization='Cardiology')
            Specialization.objects.create(specialization='Dermatology')

def create_doctor_profiles():
            user1 = User.objects.get(id=20)  
            user2 = User.objects.get(id=21)  

            doctor1 = DoctorProfile.objects.create(user=user1, personal_profile='Experienced cardiologist', rating=4, years_of_experience=10, price=150.00)
            doctor2 = DoctorProfile.objects.create(user=user2, personal_profile='Dermatologist for all skin types', rating=5, years_of_experience=8, price=120.00)

            cardiology = Specialization.objects.get(specialization='Cardiology')
            dermatology = Specialization.objects.get(specialization='Dermatology')

            doctor1.specialization.add(cardiology)
            doctor2.specialization.add(dermatology)

def create_personal_experiences():
            doctor1 = DoctorProfile.objects.get(user_id=20)
            doctor2 = DoctorProfile.objects.get(user_id=21)

            PersonalExperience.objects.create(doctor_id=doctor1, title='Cardiology Fellowship', description='Completed fellowship in cardiology at XYZ Hospital')
            PersonalExperience.objects.create(doctor_id=doctor2, title='Dermatology Residency', description='Trained in dermatology at ABC Medical Center')

def create_doctor_availabilities():
            doctor1 = DoctorProfile.objects.get(user_id=20)
            doctor2 = DoctorProfile.objects.get(user_id=21)

            DoctorAvaliability.objects.create(doctor_id=doctor1, date=date.today(), start_time=time(9, 0), end_time=time(17, 0))
            DoctorAvaliability.objects.create(doctor_id=doctor2, date=date.today(), start_time=time(10, 0), end_time=time(18, 0))

from datetime import timedelta

def doctor_avaliable_slots():
    # Get doctor profiles
    doctor1 = DoctorProfile.objects.get(user_id=20)
    doctor2 = DoctorProfile.objects.get(user_id=21)

    # Define availability time range
    start_time = time(9, 0)  # 9:00 AM
    end_time = time(17, 0)   # 5:00 PM

    # Define break time range
    break_start_time = time(12, 0)  # 12:00 PM
    break_end_time = time(13, 0)    # 1:00 PM

    # Define days of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Create availability slots for each day of the week
    for day in days_of_week:
        AvailabilitySlots.objects.create(
            doctor_id=doctor1.id,
            day_of_week=day,
            start_time=start_time,
            end_time=end_time,
            break_start_time=break_start_time,
            break_end_time=break_end_time
        )
        AvailabilitySlots.objects.create(
            doctor_id=doctor2.id,
            day_of_week=day,
            start_time=start_time,
            end_time=end_time,
            break_start_time=break_start_time,
            break_end_time=break_end_time
            
        )

        # Increment start_time, end_time, break_start_time, and break_end_time by 1 day
        # start_time += timedelta(days=1)
        # end_time += timedelta(days=1)
        # break_start_time += timedelta(days=1)
        # break_end_time += timedelta(days=1)
