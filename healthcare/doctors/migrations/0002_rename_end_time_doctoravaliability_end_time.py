# Generated by Django 5.0.4 on 2024-04-22 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctoravaliability',
            old_name='end_Time',
            new_name='end_time',
        ),
    ]