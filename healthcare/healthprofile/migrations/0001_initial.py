# Generated by Django 5.0.4 on 2024-04-15 19:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_conditions', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecificMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_medication', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(max_length=255)),
                ('medical_history', models.CharField(max_length=255)),
                ('goal', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(default=0)),
                ('fitness_level', models.PositiveIntegerField(default=0)),
                ('alcohol_use', models.IntegerField(default=0)),
                ('sleep_in_hours', models.IntegerField(default=0)),
                ('mood', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('allergies', models.ManyToManyField(blank=True, related_name='health_profiles', to='healthprofile.allergy')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('medical_condition', models.ManyToManyField(blank=True, related_name='health_profiles', to='healthprofile.medicalcondition')),
                ('specific_medication', models.ManyToManyField(blank=True, related_name='health_profiles', to='healthprofile.specificmedication')),
            ],
        ),
    ]
