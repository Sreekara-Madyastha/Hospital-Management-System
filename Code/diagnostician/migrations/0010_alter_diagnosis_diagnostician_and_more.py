# Generated by Django 4.0.1 on 2022-04-09 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostician', '0009_remove_diagnosis_labreportexists_diagnosis_labreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='Diagnostician',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diagnostician.diagnostician'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='labreport',
            field=models.BooleanField(default=False),
        ),
    ]
