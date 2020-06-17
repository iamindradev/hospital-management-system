from django.shortcuts import render
from django.http import JsonResponse
from .models import registrationd
import json
# Create your views here.
def register(request):
    if request.method=="POST":
        data_student=json.loads(request.body)
        registrationd.objects.create(**data_student)
        respone="sucess"
    return JsonResponse(respone,safe= False)
# -------------------------------------------------------------------------------------------------------------------------------------
def logind(request):
    if request.method =="POST":
        data_login_doc=json.loads(request.body)
        email=data_login_doc['email']
        password=data_login_doc['password']
        print(email)
        print(password)
        if registrationd.objects.filter(email=email, password=password).exists()==True:
            data_return=list(registrationd.objects.filter(email=email).values())
            print(data_return)
        else:
            data_return="not registerd yet"
    return JsonResponse(data_return,safe=False)
# -------------------------------------------------------------------------------------------------------------------------------------