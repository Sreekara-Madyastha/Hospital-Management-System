# Generated by Django 4.0.1 on 2022-04-10 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_assistant', '0010_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalreport',
            name='Appointment',
        ),
        migrations.RemoveField(
            model_name='medicalreport',
            name='MedicalAssistant',
        ),
        migrations.DeleteModel(
            name='MedicalAssistant',
        ),
        migrations.DeleteModel(
            name='MedicalReport',
        ),
    ]
