# Generated by Django 4.0.1 on 2022-10-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorApp', '0005_remove_appointment_time_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Schedule',
            field=models.CharField(default='8-10', max_length=200),
        ),
    ]
