# Generated by Django 4.0.1 on 2022-04-10 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostician', '0013_diagnosis'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Diagnosis',
        ),
        migrations.DeleteModel(
            name='Diagnostician',
        ),
    ]
