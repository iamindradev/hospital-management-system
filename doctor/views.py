from django.shortcuts import render
from django.http import JsonResponse
from .models import registrationd
from patient.models import appointment, registrationp
import json
# reister
def register(request):
    if request.method == "POST":
        data_doctor = json.loads(request.body)
        registrationd.objects.create(**data_doctor)
        respone="sucess"
    return JsonResponse(respone,safe = False)
#login
def logind(request):
    if request.method == "POST":
        data_login_doc = json.loads(request.body)
        email = data_login_doc['email']
        password = data_login_doc['password']
        #to do filter status
        print(email)
        print(password)
        if registrationd.objects.filter(email = email, password = password).exists() == True:
            data_return=list(registrationd.objects.filter(email = email).values())
            print(data_return)
        else:
            data_return = "not registerd yet"
    return JsonResponse(data_return,safe = False)

# pending request
def pending_appointments(request):
    if request.method == "GET":
        data_of_appointment = appointment.object.filter(status="approved_by_manager").value('disease',
        'date_for_app','time_for_app',).order_by('date_time_of_app')
    return JsonResponse(data_of_appointment , safe = False)

    
