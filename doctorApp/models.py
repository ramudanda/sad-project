from datetime import date
from enum import unique
from django.db import models


class Users(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    Name=models.CharField(max_length=200, default='')
    email=models.EmailField(default='')
    Date=models.DateField()
    Phone=models.CharField(max_length=15)
    Doctor=models.CharField(max_length=15, default='John')
    Schedule=models.CharField(max_length=200, default='8:00AM-10:00AM')
    Disease = models.CharField(max_length = 200, default='Cold')

    def __str__(self):
        return self.Name
    
# Create your models here.
