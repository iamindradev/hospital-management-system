from django.shortcuts import render
from django.http import JsonResponse
from .models import registration
import json

def register(request):
    if request.method=="POST":
        data_register=json.loads(request.body)
        # for creation of medical id from input data
        # fname=data_register[first_name]
        # lname=data_register[last_name]
        # mob_num=data_register[mobile_number]
        # medical_id=fname[0:1]+lname[0:1]+mob_num[7:11]
        registration.objects.create(**data_register)
        response="sucess"
    return JsonResponse(response,safe= False)

def loginp(request):
    if (request.method)=="POST":
        data_for_login=json.loads(request.body)
        email_id= data_for_login['email']
        password= data_for_login['password']
        print(email_id, password)
        login =registration.objects.filter(email=email_id, password=password)
        if login!= "NULL":
        # registration.objects.create(**data_for_login)
            response="sucees"
        else:
            response="not registered"
    return JsonResponse(response ,safe=False)
