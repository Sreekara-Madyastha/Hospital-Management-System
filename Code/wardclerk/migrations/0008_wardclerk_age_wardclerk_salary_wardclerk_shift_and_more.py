# Generated by Django 4.0.1 on 2022-04-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardclerk', '0007_warddetails_totalbill_warddetails_wardbill'),
    ]

    operations = [
        migrations.AddField(
            model_name='wardclerk',
            name='Age',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='wardclerk',
            name='Salary',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='wardclerk',
            name='Shift',
            field=models.IntegerField(default=None),
        ),
        migrations.DeleteModel(
            name='WardDetails',
        ),
    ]
