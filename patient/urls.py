from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),#url for patient registration
    path('login/', views.loginp, name='login'),#url for patient login
    path('notifications/', views.notifi, name='notifications'),#url for all notifications
    path('make_appointment/', views.make_appointment ,name='submit_appointmenrt'),#url for submit appoint at the tim of making appointment
    path('cancel_appointment/', views.cancelapp, name="cancel_apptment"),#cancel of appointment by patient
    path('often/',views.often, name="often"),#for 
    path('all_report/',views.all_report,name="all_report"),
    path('appointment_history/',views.all_appointments, name="appointment_history"),
    path('multiple/', views.multiple,name='bla')
]
