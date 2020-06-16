from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginp, name='login'),
    # path('make_appointmet/' views.make_appointment , name='make_appointment'),
    path('submit_appointment/', views.submit_appointment ,name='save_appointmenrt')
]
