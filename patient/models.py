from django.db import models

# Create your models here.
class registrationp(models.Model):
   first_name= models.CharField(max_length=200)
   last_name= models.CharField(max_length=200)
   email=models.EmailField(max_length=254)
   mobile_number=models.CharField( max_length=50)
   password= models.CharField( max_length=50)
   age=models.IntegerField()
   blood_group=models.CharField(max_length=50)
   gender=models.CharField(max_length=50)
   height=models.IntegerField()
   weight=models.IntegerField()
   medical_history=models.CharField( max_length=50)
   user_type=models.CharField( max_length=50, default='patient')
   status=models.CharField(default="pending",max_length=50)
   # medical_id=models.CharField(max_length=50)

class medicine(models.Model):
   date=models.DateField(auto_now_add=False)
   medicine_given=models.CharField( max_length=255)
   medication_for=models.CharField( max_length=50)
   doctor_name=models.CharField( max_length=50)


class appointment(models.Model):
   patient=models.ForeignKey(registrationp,  on_delete="DO_NOTHING", null= True)
   date_time_of_app=models.DateTimeField(auto_now_add=True)
   disease= models.CharField(max_length=50)
   date_for_app = models.DateField()
   time_for_app=models.TimeField()
   doctor=models.CharField(max_length=50)
   status=models.CharField(max_length=50, default="pending")
   



   
