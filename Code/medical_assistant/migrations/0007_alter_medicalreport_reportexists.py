# Generated by Django 4.0.1 on 2022-04-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_assistant', '0006_remove_medicalreport_report_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalreport',
            name='reportexists',
            field=models.FileField(default=None, upload_to='medical_report/'),
        ),
    ]
