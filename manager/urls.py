from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginm , name = 'login'),
    path('all_patient/', views.all_patient,name='all_patient'),
    path('all_doctor/', views.all_doctor, name='all_doctor'),
    path('pending_appointments/', views.pending_app ,name='pending_app'),
    path('doctor_approval/',views.doctor_approval, name='doctor_approval')  
]
