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
            pending_appointment=appointment.objects.filter(status="pending").count()
            pending_registration=registrationd.objects.filter(status="pending").count()
            data={
                "pending_appointment":pending_appointment,
                "pending_registration":pending_registration}
            print(data)
        else:
            data="you are not manager"
    return JsonResponse(data, safe= False)
# --------------------------------------------------------------------------------------------------------------------------------------
def all_patient(request):
    if request.method=="GET":
        patient_list=list(registrationp.objects.values('first_name','last_name','age','mobile_number','email'))
        print(patient_list)
    return JsonResponse(patient_list,safe=False)

# --------------------------------------------------------------------------------------------------------------------------------------
def all_doctor(request):
    if request.method=="GET":
        doctor_list=list(registrationd.objects.values('first_name','last_name','qualification','previous_exp','email'))
        print(doctor_list)
    return JsonResponse(doctor_list,safe=False)
        
# --------------------------------------------------------------------------------------------------------------------------------------
def doctor_approval(request):
    if request.method =="GET":
        data_to_approve=list(registrationd.objects.filter(status="pending").values('first_name','last_name','qualification',
        'previous_exp','email','gender','mobile_number'))
        print(data_to_approve)
    return JsonResponse(data_to_approve,safe=False)

#-----------------------------------------------------------------------------------------------------------------------------------------
def pending_app(request):
    if request.method =="GET":
        data_to_approve=list(appointment.objects.filter(status="pending").values('disease','date_for_app','time_for_app',).order_by('date_time_of_app'))
        print(data_to_approve)
    return JsonResponse(data_to_approve,safe=False)



