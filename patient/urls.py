from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),#url for patient registration
    path('login/', views.loginp, name='login'),#url for patient login
    path('notifications/', views.notifi, name='notifications'),#url for all notifications
    path('make_appointment/', views.make_appointment ,name='submit_appointmenrt')#url for submit appoint at the tim of making appointment
]
