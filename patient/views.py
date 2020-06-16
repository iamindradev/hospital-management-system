from django.shortcuts import render
from django.http import JsonResponse
from doctor.models import registrationd
from .models import registrationp, appointment
from django.core.exceptions import ObjectDoesNotExist
import json

def register(request):
    if request.method=="POST":
        data_register=json.loads(request.body)
        # for creation of medical id from input data
        # fname=data_register[first_name]
        # lname=data_register[last_name]
        # mob_num=data_register[mobile_number]
        # medical_id=fname[0:1]+lname[0:1]+mob_num[7:11]
        registrationp.objects.create(**data_register)
        response="sucess"
    return JsonResponse(response,safe= False)Variable
#--------------------------------------------------------------------------------------------------------------------------------
def loginp(request):
    if (request.method)=="POST":
        data_for_login=json.loads(request.body)
        email_id= data_for_login['email']
        password= data_for_login['password']
        print(email_id, password)
        login =registrationp.objects.filter(email=email_id, password=password)
        if login!= "NULL":
            try:
                data_to_return=list(registrationp.objects.filter(email= email_id).values())
                print(data_to_return)
            except ObjectDoesNotExist:
                print("does not exist")
        # registration.objects.create(**data_for_login)
            # response="sucees"
            # else:
            #     data_to_return="not registered"
    return JsonResponse(data_to_return ,safe=False)

#----------------------------------------------------------------------------------------------------------------------------
def make_appointment(request):
    if request.method =="GET":
        list_of_doctor= registrationd.objects.all()
    return JsonResponse(list_of_doctor)

#----------------------------------------------------------------------------------------------------------------------------
def submit_appointment(request):
    if request.method=="POST":
        data_of_app= json.loads(request.body)
        appointment.objects.create(**data_of_app).exclude(doct)