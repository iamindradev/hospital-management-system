from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),#url for patient registration
    path('login/', views.loginp, name='login'),#url for patient login
    # path('all_data/', views.all_data, name='all_data'),#url for fetchin all data
    path('make_appointment/', views.make_appointment ,name='submit_appointmenrt')#url for submit appoint at the tim of making appointment
    
]
