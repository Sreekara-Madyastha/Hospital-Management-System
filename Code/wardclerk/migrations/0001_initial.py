# Generated by Django 3.2.7 on 2022-04-01 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('WardType', models.CharField(default='usual', max_length=45, primary_key=True, serialize=False)),
                ('WardCapacity', models.IntegerField()),
                ('Population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WardClerk',
            fields=[
                ('WardClerkID', models.IntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=45)),
                ('LastName', models.CharField(max_length=45)),
                ('EmailAddress', models.CharField(max_length=45)),
                ('PermantAddress', models.CharField(max_length=100)),
                ('BloodGroup', models.CharField(max_length=45)),
                ('contact', models.CharField(default=None, max_length=13)),
                ('Ward', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wardclerk.ward')),
            ],
        ),
    ]
