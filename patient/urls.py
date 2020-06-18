from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginp, name='login'),
    path('all_data/', views.all_data, name='all_data'),
    path('submit_appointment/', views.submit_appointment ,name='submit_appointmenrt')
    
]
