# Generated by Django 4.0.1 on 2022-04-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Age',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Salary',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Shift',
            field=models.IntegerField(default=None),
        ),
    ]
