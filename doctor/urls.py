from django.urls import path 
from .import views

urlpatterns = [
    path('register/' ,views.register, name='register'),
    path('login/', views.logind, name="login"),
    path('pending_appointments/', views.pending_appointments ,name='pending_app'),#for showing the details of pending appointment of patient
    path('approve_appointments/',views.approve_appointment ,name='approve_app'), #for modification and approval of apponintment of patient
]
