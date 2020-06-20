from django.shortcuts import render
from patient.models import appointment, registrationp,notification
from doctor.models import registrationd
from django.http import JsonResponse
from .models import login
import json

#for login
def loginm(request):
    if request.method == "POST":
        data = json.loads(request.body)
        uname = data['username']
        passwd = data['password']
        if login.objects.filter(username = uname , password = passwd).exists() == True:
            pending_appointment = appointment.objects.filter(status = "pending").count()
            pending_registration = registrationd.objects.filter(status = "pending").count()
            data={
                "pending_appointment":pending_appointment,
                "pending_registration":pending_registration}
            # print(data)
        else:
            data = "you are not manager"
    return JsonResponse(data, safe = False)

#for fetching all patient on manager ds
def all_patient(request):
    if request.method == "GET":
        patient_list = list(registrationp.objects.values('first_name','last_name','age','mobile_number','email'))
        # print(patient_list)
    return JsonResponse(patient_list,safe=False)

#for fetching all doctor on manager ds
def all_doctor(request):
    if request.method=="GET":
        doctor_list=list(registrationd.objects.filter(status="approved").values('first_name','last_name','qualification','previous_exp','email'))
        # print(doctor_list)
    return JsonResponse(doctor_list,safe=False)
        

#for apporoval of doctor registration
def doctor_approval(request):
    if request.method =="GET":
        data_to_approve=list(registrationd.objects.filter(status="pending").values('first_name','last_name','qualification',
        'previous_exp','email','gender','mobile_number'))
        # print(data_to_approve)
    return JsonResponse(data_to_approve,safe=False)

#for pending appointment of patient
def pending_appointment(request):
    if request.method =="GET":
        data_to_approve = list(appointment.objects.filter(status="pending").values('disease','date_for_app','time_for_app',
        'patient_id').order_by('date_time_of_app'))
        # print(data_to_approve)
    return JsonResponse(data_to_approve,safe=False)

#for approval of registration of doctor
def approve_registration(request):
    if request.method=="POST":
        data= json.loads(request.body)
        email=data['email']
        status=data['activity']
        if status=="approved":
            registrationd.objects.filter(email=email).update(status="approved")
            response="approved"
        else:
            registrationd.objects.filter(email=email).update(status="rejected")
            response="rejected"
    return JsonResponse(response,safe=False)


#for approval of appointment
def approve_appointment(request):
    if request.method=="POST":
        data= json.loads(request.body)
        patient_id=data["patient_id"]
        status=data['activity']
        id=data['doct_key_id']
        print(id)
        print(data)
        if id != "NULL":
            if status=="approved":
                appointment.objects.filter(patient_id=patient_id).update(status="approved_by_manager",doct_key_id=id)
                response="approved"
            elif status=="modified":
                date_for_app = data['date_for_app']
                time_for_app = data['time_for_app']
                appointment.objects.filter(patient_id=patient_id).update(date_for_app=date_for_app,time_for_app=time_for_app,
                doct_key_id=id,status="approved_by_manager")
                notification.objects.create(changes_made="rejected_by_manager")
                response="modified"
        else:
            response="not assigned doctor"
    return JsonResponse(response,safe=False)       

#reject approval
def reject_appointment(request):
    if request.method =="POST":
        data= json.loads(request.body)
        patient_id=data["patient_id"]
        status=data['activity']
        appointment.objects.filter(patient_id=patient_id).update(status="rejected")
        notification.objects.create(changes_made="rejected_by_manager")
        response="rejected"
    return JsonResponse(response,safe=False)

#for assignment of department
def assign_department(request):
    if request.method=="GET":
        department= list(registrationd.objects.filter(status="approved").values("department"))
        print(department)
    return JsonResponse(department,safe=False)

#for assignment of doctor
def assign_doctor(request):
    if request.method=="POST":
        data=json.loads(request.body)
        dept=data['department']
        doctor= list(registrationd.objects.filter(status="approved",department=dept).values("first_name","last_name","id"))
        # print(doctor)
    return JsonResponse(doctor ,safe= False)




    