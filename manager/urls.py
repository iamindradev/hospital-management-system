from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginm , name = 'login'),#for manager login
    path('all_patient/', views.all_patient,name='all_patient'),#for displaying all patient on ds of manager
    path('all_doctor/', views.all_doctor, name='all_doctor'),#for displaying all doctor on ds of manager
    path('pending_appointments/', views.pending_appointment ,name='pending_app'),#for showing the details of pending appointment of patient
    path('doctor_approval/',views.doctor_approval, name='doctor_approval'),#for showing the details of pening registration of doctor
    path('approve_registration/',views.approve_registration,name='approve_regist'),#for recieving the data of approval or rejection of doctor
    path('approve_appointment/', views.approve_appointment, name="approve_appointment"),#for recieving the data of approval or rejection of patient
    path('assign_doctor/',views.assign_doctor,name='doctor'),#for sending the data of doctor for assignment of patient
    path('assign_department/',views.assign_department, name="department",)#for sending the data of department for assignment of patient.
]
