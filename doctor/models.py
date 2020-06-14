from django.db import models

# Create your models here.
class registration(models.Model):
   first_name= models.CharField(max_length=200)
   last_name= models.CharField(max_length=200)
   email=models.EmailField(max_length=254)
   mobile_number=models.CharField( max_length=50)
   password= models.CharField( max_length=50)
   age=models.IntegerField()
   gender=models.CharField(max_length=50)
   medical_id=models.CharField(max_length=50)
   qualification=models.CharField(max_length=50,null= True)
   status=models.CharField(max_length=50, default="pending")
   previous_exp=models.IntegerField(null= True)



