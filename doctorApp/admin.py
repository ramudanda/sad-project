from django.contrib import admin

from .models import Appointment

# # Register your models here.

class appointment(admin.ModelAdmin):
    list_display=['Name', 'email', 'Phone', 'Date','Schedule', 'Doctor', 'Disease']
    ordering=('-Date',)


admin.site.register(Appointment, appointment)