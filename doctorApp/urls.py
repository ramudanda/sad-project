from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registrationPage, name='register'),
    path('login/', views.loginpage, name='login'),   
    path('apoint/', views.appointment, name='apointt'),
    path('book/',views.book, name='book'),
    
]