from django.shortcuts import render
from 
from django.http import JsonResponse
from .models import login
import json

# Create your views here.

def loginm(request):
    if request.method =="POST":
        data= json.loads(request.body)
        uname= data['username']
        passwd= data['password']
        if login.objects.filter(username = uname , password= passwd).exist()==True:
            print(uname)
            print(passwd)
            pending_appointment=
            resp="hey"
            
    return JsonResponse(resp, safe= False)
