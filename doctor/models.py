from django.db import models

# Create your models here.
class registrationd(models.Model):
   first_name= models.CharField(max_length=200)
   last_name= models.CharField(max_length=200)
   email=models.EmailField(max_length=254)
   mobile_number=models.CharField( max_length=50)
   password= models.CharField( max_length=50)
   age=models.IntegerField()
   gender=models.CharField(max_length=50)
   qualification=models.CharField(max_length=50,null= True)
   department= models.CharField(max_length = 150,null=True)
   status=models.CharField(max_length=50, default="pending")
   previous_exp=models.IntegerField(null= True)

class report(models.Model):
   date_of_report = models.DateField(auto_now=True)
   time_of_report = models.TimeField(auto_now=True)
   appntment = models.ForeignKey('patient.appointment', on_delete="DO_NOTHING", null= True)
   prescription = models.CharField(max_length = 150)
   further_ins = models.CharField(max_length = 150, null= True)
   


   
