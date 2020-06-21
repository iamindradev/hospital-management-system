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
   # user_type=models.CharField( max_length=50, default='patient')

# class medicine(models.Model):
#    date=models.DateField(auto_now_add=False)
#    medicine_given=models.CharField( max_length=255)
#    medication_for=models.CharField( max_length=50)
#    doctor_name=models.CharField( max_length=50)


class appointment(models.Model):
   patient=models.ForeignKey('registrationp', db_column='patient_id' , on_delete="DO_NOTHING",null=True)
   doct_key= models.ForeignKey('doctor.registrationd', on_delete="DO_NOTHING", null= True)
   date_time_of_app=models.DateTimeField(auto_now_add=True)
   disease= models.CharField(max_length=50)
   date_for_app = models.DateField()
   time_for_app=models.TimeField()
   status=models.CharField(max_length=50, default="pending")



#class for notification of status of appointment by patient
class notification(models.Model):
   date_of_notification = models.DateField(auto_now_add=True)
   time_of_notification = models.TimeField(auto_now_add=True)
   changes_made = models.CharField(max_length = 150,default="pending")
   change_made_by = models.CharField(max_length = 150, null= True)
   status = models.CharField(max_length = 150, default="active")
   appntment = models.ForeignKey('appointment', on_delete="DO_NOTHING", null= True)
   
   
   
   
   
   
   



   
