from django.shortcuts import render
from django.http import JsonResponse
from .models import registration
import json
# Create your views here.
def register(request):
    if request.method=="POST":
        data_student=json.loads(request.body)
        #for creation of medical id from input data
        # fname=data_register[first_name]
        # lname=data_register[last_name]
        # mob_num=data_register[mobile_number]
        # medical_id=fname[0:1]+lname[0:1]+mob_num[7:11]
        registration.objects.create(**data_student)
        respone="sucess"
    return JsonResponse(respone,safe= False)

def logind(request):
    if request.method =="POST":
        data_login_doc=json.loads(request.body)
        email=data_login_doc['email']
        password=data_login_doc['password']
        if registration.objects.filter(email=email, password=password).exists()==True:
            response="logged in successfully"
        else:
            response="not registerd yet"
    return JsonResponse(response,safe=False)