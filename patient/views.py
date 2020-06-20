from django.shortcuts import render
from django.http import JsonResponse
from doctor.models import registrationd
from .models import registrationp, appointment
from django.core.exceptions import ObjectDoesNotExist
import json
#registration of patient
def register(request):
    if request.method=="POST":
        data_register=json.loads(request.body)
        registrationp.objects.create(**data_register)
        response="sucess"
    return JsonResponse(response,safe= False)

#login of patient
def loginp(request):
    if (request.method)=="POST":
        data_for_login=json.loads(request.body)
        email_id= data_for_login['email']
        password= data_for_login['password']
        print(email_id, password)
        if registrationp.objects.filter(email=email_id).exists() == True:
            if registrationp.objects.filter(email=email_id, password=password).exists() == True:
                data_to_return =list(registrationp.objects.filter(email=email_id).values('first_name',
                'last_name','email','mobile_number','age','blood_group','gender','height','weight',))
                # print(data_to_return)
            else:
                data_to_return="wrong password"
        else:
            data_to_return="not registered"
    
    return JsonResponse(data_to_return ,safe=False)

#make appointment
def make_appointment(request):
    if request.method=="POST":
        data_of_app= json.loads(request.body)
        email=data_of_app["email"]
        disease=data_of_app['disease']
        date_for_app=data_of_app['date_for_app']
        time_for_app=data_of_app['time_for_app']
        patient=list(registrationp.objects.filter(email=email).values('id'))
        id_dict=patient[0]
        patient_id=id_dict["id"]
        print(patient_id)
        print(list(data_of_app))
        appointment.objects.create(disease=disease,date_for_app=date_for_app,time_for_app=time_for_app,patient_id=patient_id)
        response="added"
    return JsonResponse(response, safe= False)

#----------------------------------------------------------------------------------------------------------------------------
# def all_data(request):
#     if request.method=="GET":
#         data= list(appointment.object.filter())
#     return JsonResponse(data, safe= False)