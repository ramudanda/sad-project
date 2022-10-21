from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment
from django.forms import ModelForm





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields =['Name', 'email', 'Date', 'Time', 'Phone']
#         # widgets = {
        #     'Name': forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px; color:white;background-color:blue', 'class': 'form-control'}),
        #     'email':forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;color:white', 'class': 'form-control'}),
        #     'Date':forms.DateInput(attrs={'placeholder': 'Date', 'style': 'width: 300px;color:white', 'class': 'form-control', 'type':'date'}),
        #     'Time':forms.TimeInput(attrs={'placeholder': 'Time', 'style': 'width: 300px;color:white', 'class': 'form-control', 'type':'time'}),
        #     'Phone':forms.NumberInput(attrs={'placeholder': 'Phone', 'style': 'width: 300px;color:white;background-color:blue', 'class': 'form-control'}),

        # }
        # labels ={'Name':'', 'email':'', 'Date':'', 'Time':'','Phone':''}


