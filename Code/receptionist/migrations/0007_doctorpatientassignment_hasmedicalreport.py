# Generated by Django 4.0.1 on 2022-04-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0006_doctorpatientassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorpatientassignment',
            name='hasmedicalreport',
            field=models.BooleanField(default=False),
        ),
    ]