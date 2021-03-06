# Generated by Django 4.0.1 on 2022-04-07 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
        ('receptionist', '0005_delete_doctorpatientassignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorPatientAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AppointmentID', models.IntegerField(default=None)),
                ('VisitNo', models.IntegerField(default=None)),
                ('datetime', models.DateTimeField(default=None)),
                ('status', models.CharField(default='Unattended', max_length=10)),
                ('Doctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('Patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('Receptionist', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='receptionist.receptionist')),
            ],
            options={
                'unique_together': {('AppointmentID', 'VisitNo')},
            },
        ),
    ]
