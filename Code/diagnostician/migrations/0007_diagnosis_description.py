# Generated by Django 4.0.1 on 2022-04-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostician', '0006_rename_document_diagnosis_labreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='description',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
