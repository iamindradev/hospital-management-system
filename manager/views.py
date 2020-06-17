from django.shortcuts import render
from patient.models import appointment, registrationp
from doctor.models import registrationd
from django.http import JsonResponse
from .models import login
import json

# Create your views here.

def loginm(request):
    if request.method =="POST":
        data= json.loads(request.body)
        uname= data['username']
        passwd= data['password']
        if login.objects.filter(username = uname , password= passwd).exists()==True:
    #         print(uname)
    #         print(passwd)
            pending_appointment=["hey"]
            pending_registration=list(registrationd.objects.filter(status="pending").values())
            data={pending_appointment,pending_registration}
               # pending_appointment=appointment.
    return JsonResponse(data, safe= False)
def all_patient(request):
    if request.method=="GET":
        patient_list=list(registrationp.objects.values('first_name','last_name','age','mobile_number','email'))
        print(patient_list)
    return JsonResponse(patient_list,safe=False)


def all_doctor(request):
    if request.method=="GET":
        doctor_list=list(registrationd.objects.values('first_name','last_name','qualification','previous_exp','email'))
        print(doctor_list)
    return JsonResponse(doctor_list,safe=False)
        


