from django.db import models

# Create your models here.
class registration(models.Model):
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


   
