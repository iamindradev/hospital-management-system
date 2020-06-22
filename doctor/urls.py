from django.urls import path 
from .import views

urlpatterns = [
    path('register/' ,views.register, name='register'),
    path('login/', views.logind, name="login"),
    path('pending_appointments/', views.pending_appointments ,name='pending_app'),#for showing the details of pending appointment of patient
    path('approve_appointments/',views.approve_appointment ,name='approve_app'), #for modification and approval of apponintment of patient
    path('generate_report/', views.generate_report, name='generate'),
    path('submit_report/',views.submit_report,name='submit_report'),
    path('get_report/',views.get_report, name='get_report'),
    path('patient_list/',views.patient_list, name='patient_list'),
    path('report_list/', views.report_list, name='report_list')
]
