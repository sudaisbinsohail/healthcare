from django.core.management.base import BaseCommand
from django.utils import timezone
from healthcare.healthprofile.models import Allergy, MedicalCondition, SpecificMedication


allergy_names = [
            "Allergy 1",
            "Allergy 2",
            "Allergy 3",
            "Allergy 4",
            "Allergy 5",
            "Allergy 6",
            "Allergy 7",
            "Allergy 8",
            "Allergy 9",
            "Allergy 10"
        ]
medical_condition_names = [
            "Condition 1",
            "Condition 2",
            "Condition 3",
            "Condition 4",
            "Condition 5",
            "Condition 6",
            "Condition 7",
            "Condition 8",
            "Condition 9",
            "Condition 10"
        ]
specific_medication_names = [
            "Medication 1",
            "Medication 2",
            "Medication 3",
            "Medication 4",
            "Medication 5",
            "Medication 6",
            "Medication 7",
            "Medication 8",
            "Medication 9",
            "Medication 10"
        ]

   

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **options):


        def generate_timestamp():
            return timezone.now()

        for name in allergy_names:
            Allergy.objects.create(
                allergy=name,
                created_at=generate_timestamp(),
                updated_at=generate_timestamp()
            )

        for name in medical_condition_names:
            MedicalCondition.objects.create(
                medical_conditions=name,
                created_at=generate_timestamp(),
                updated_at=generate_timestamp()
            )
        for name in specific_medication_names:
            SpecificMedication.objects.create(
                specific_medication=name,
                created_at=generate_timestamp(),
                updated_at=generate_timestamp()
            )

        self.stdout.write(self.style.SUCCESS('Database seeding complete'))
