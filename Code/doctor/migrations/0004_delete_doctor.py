# Generated by Django 4.0.1 on 2022-04-10 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0015_delete_doctorpatientassignment_delete_receptionist'),
        ('medical_assistant', '0013_remove_medicalreport_appointment_and_more'),
        ('doctor', '0003_doctor_age_doctor_salary_doctor_shift'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
