# Generated by Django 4.0.1 on 2022-04-10 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_technician', '0004_pharmacybill'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PharmacyBill',
        ),
        migrations.DeleteModel(
            name='PharmacyTechnician',
        ),
    ]
