from django.shortcuts import render
from django.http import JsonResponse
from .models import registrationd
from patient.models import appointment, registrationp
import json
# reister
def register(request):
    if request.method == "POST":
        data_doctor = json.loads(request.body)
        # registrationd.objects.create(**data_doctor)
        respone="sucess"
    return JsonResponse(respone,safe = False)
#login doctor
def logind(request):
    if request.method == "POST":
        data_login_doc = json.loads(request.body)
        email = data_login_doc['email']
        password = data_login_doc['password']
        if registrationd.objects.filter(status = "approved",email=email).exists() == True:
            if registrationd.objects.filter(status = "approved",email=email,password=password).exists()==True:
                data_list = list(registrationd.objects.filter(status = "approved",email=email,password=password).values("email","password"))
                data = data_list[0]
                passwd = data["password"]
                print(passwd)
                if password ==passwd :
                    print(data)  
                    data_r=list(registrationd.objects.filter(email = email).values("first_name","last_name",
                    "email","mobile_number","age","gender","previous_exp","qualification","department","id"))
                    pending_appointment = appointment.objects.filter(status = "approve_by_manager").count()
                    data_return={"data_r":data_r, "pending_appointment":pending_appointment}
                    return JsonResponse(data_return ,safe = False)
                    print(data_return)
            else:
                data_return="wrong password"
        else:
            data_return = "not registerd"
    return JsonResponse(data_return ,safe = False)

#pending appointments
def pending_appointments(request):
    if request.method == "POST":
        data=json.loads(request.body)
        doct_key_id= data['id']
        print(doct_key_id)
        data_of_appointment = list(appointment.objects.filter(status__contains="approved_by_manager",doct_key_id=doct_key_id).values('disease',
        'date_for_app','time_for_app',"patient_id").order_by('date_time_of_app'))
        print(data_of_appointment)
    return JsonResponse(data_of_appointment , safe = False)


#modified appointments
def approve_appointment(request):
    if request.method =="POST":
        data= json.loads(request.body)
        patient_id=data['id']
        status=data['activity']
        if status=="approved":
            appointment.objects.filter(patient_id=patient_id).update(status="approved_by_both",doct_key_id=id)
            response="approved"
        elif status=="modified":
            date_for_app = data['date_for_app']
            time_for_app = data['time_for_app']
            appointment.objects.filter(patient_id=patient_id).update(date_for_app=date_for_app,time_for_app=time_for_app,
            doct_key_id=id,status="approved_by_doctor")
            response="modified"
    return JsonResponse(response,safe=False)          


#reject approval
def reject_appointment(request):
    if request.mehtod =="POST":
        data= json.loads(request.body)
        patient_id=data["patient_id"]
        status=data['activity']
        appointment.objects.filter(patient_id=patient_id).update(status="rejected_by_doctor")
        response="rejected"
    return JsonResponse(response,safe=False)