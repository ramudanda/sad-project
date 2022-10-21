# Generated by Django 4.0.1 on 2022-10-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorApp', '0011_remove_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='Doctor',
            field=models.CharField(default='John', max_length=15),
        ),
        migrations.AddField(
            model_name='appointment',
            name='Schedule',
            field=models.CharField(default='8:00AM-10:00AM', max_length=200),
        ),
    ]