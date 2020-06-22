from django.shortcuts import render
from django.http import JsonResponse
from .models import registrationd,report
from patient.models import appointment, registrationp,notification
import json
# reister
def register(request):
    if request.method == "POST":
        data_doctor = json.loads(request.body)
        registrationd.objects.create(**data_doctor)
        respone="success"
    return JsonResponse(respone,safe = False)
#login doctor
def logind(request):
    if request.method == "POST":
        data_login_doc = json.loads(request.body)
        email = data_login_doc['email']
        password = data_login_doc['password']
        if registrationd.objects.filter(status = "approved",email=email).exists() == True:
            if registrationd.objects.filter(status = "approved",email=email,password=password).exists()==True:
                data_list = list(registrationd.objects.filter(status = "approved",email=email,password=password)
                .values("email","password"))
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
        data_of_appointment = list(appointment.objects.filter(status__contains="approved_by_manager",doct_key_id=
        doct_key_id).values('disease','date_for_app','time_for_app',"patient_id").order_by('date_time_of_app'))
        print(data_of_appointment)
    return JsonResponse(data_of_appointment , safe = False)


#modified appointments
def approve_appointment(request):
    if request.method =="POST":
        data= json.loads(request.body)
        patient_id=data['patient_id']
        status=data['activity']
        appntment = appointment.objects.filter(patient_id=patient_id).values()
        appointment_data= appntment[0]
        appointment_id=appointment_data["id"]
        print(patient_id, status)
        if status=="approved":
            appointment.objects.filter(patient_id=patient_id).update(status="approved_by_both")
            notification.objects.create(changes_made="approved",changes_made_by="doctor",status="active",appntment_id=
            appointment_id)
            response="approved"
            return JsonResponse(response,safe=False) 
        elif status=="modified":
            date_for_app = data['date_for_app']
            time_for_app = data['time_for_app']
            appointment.objects.filter(patient_id=patient_id).update(date_for_app=date_for_app,time_for_app=time_for_app,
            status="approved_by_both")
            notification.objects.create(changes_made="modified",changes_made_by="doctor",status="active",appntment_id=
            appointment_id)
            response="modified"
            return JsonResponse(response,safe=False)          


#reject approval
def reject_appointment(request):
    if request.mehtod =="POST":
        data= json.loads(request.body)
        patient_id=data["patient_id"]
        status=data['activity']
        appntment = appointment.objects.filter(patient_id=patient_id).values()
        appointment_data= appntment[0]
        appointment_id=appointment_data["id"]
        appointment.objects.filter(patient_id=patient_id).update(status="rejected_by_doctor")
        notification.objects.create(changes_made="rejected",changes_made_by="doctor",status="active",appntment_id=
        appointment_id)
        response="rejected"
    return JsonResponse(response,safe=False)
#genrate report
def generate_report(request):
    if request.method=="POST":
        data=json.loads(request.body)
        doct_key_id=data['id']
        response=list(appointment.objects.filter(doct_key_id=doct_key_id,status_of_report="pending",status="approved_by_both").values('id', 
        'date_for_app','disease','time_for_app'))
    print(response)
    return JsonResponse(response ,safe= False)
#submit report
def submit_report(request):
    if request.method=="POST":
        data_=json.loads(request.body)
        appntment_id=data_['appntment_id']
        # print(data_)
        report.objects.create(**data_)
        appointment.objects.filter(id=appntment_id).update(status_of_report="generated")
        response="report created"
    return JsonResponse(response, safe= False)
#get report of patient after creating by doctor
def get_report(request):
    if request.method=="POST":
        data= json.loads(request.body)
        appntment_id = data['appntment_id']
        report_data=list(report.objects.filter(appntment_id=appntment_id).values('prescription', 'further_ins','date_of_report',
        'appntment_id__doct_key_id__first_name','appntment_id__doct_key_id__last_name','appntment_id__disease','time_of_report',
        'appntment_id__patient_id__first_name','appntment_id__patient_id__last_name','appntment_id__doct_key_id__department',
        ))
    return JsonResponse(report_data, safe=False)
#patient list whose request has been created
def report_list(request):
    if request.method =="POST":
        data = json.loads(request.body)
        doct_key_id=data['id']
        list_data=list(appointment.objects.filter(doct_key_id=doct_key_id, status_of_report="generated",status="approved_by_both").
        values('id','patient_id__first_name','patient_id__last_name','disease','date_for_app','time_for_app'))
    return JsonResponse(list_data,safe= False)


#patient list under individual doctor created
def patient_list(request):
    if request.method =="POST":
        data = json.loads(request.body)
        doct_key_id=data['id']
        list_data=list(appointment.objects.filter(doct_key_id=doct_key_id).values('id','patient_id__first_name','patient_id',
        'patient_id__age','patient_id__mobile_number','patient_id__last_name','patient_id__count'))
    return JsonResponse(list_data,safe= False)      