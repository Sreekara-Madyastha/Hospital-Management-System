# Generated by Django 4.0.1 on 2022-04-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Shift',
            field=models.IntegerField(default=0),
        ),
    ]
