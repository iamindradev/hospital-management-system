from django.shortcuts import render
from django.http import JsonResponse
from doctor.models import registrationd, report
from .models import registrationp, appointment,notification
from django.core.exceptions import ObjectDoesNotExist
import json
from django.db.models import Count, Max
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
                'last_name','email','mobile_number','age','blood_group','gender','height','weight','id'))
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
        patient=list(registrationp.objects.filter(email=email).values('id'))
        id_dict=patient[0]
        patient_id=id_dict["id"]
        if appointment.objects.filter(patient_id=patient_id,status="pending").exists() == True:
            response="you already have a pending appointment"
            return JsonResponse(response, safe= False)

        else:  
            disease=data_of_app['disease']
            date_for_app=data_of_app['date_for_app']
            time_for_app=data_of_app['time_for_app']
            # print(patient_id)
            # print(list(data_of_app))
            appointment.objects.create(disease=disease,date_for_app=date_for_app,time_for_app=time_for_app,patient_id=patient_id)
            response="added"
            return JsonResponse(response, safe= False)

#notification
def notifi(request):
    if request.method =="POST":
        data= json.loads(request.body)
        patient_id =data['id']
        if notification.objects.filter(appntment_id__patient_id=patient_id, status="active").exists() == True:
            active_noti = list(notification.objects.filter(appntment_id__patient_id=patient_id).values('date_of_notification',
            'time_of_notification','changes_made','changes_made_by').order_by('-time_of_notification','-date_of_notification'))
            notification.objects.filter(appntment_id__patient_id=patient_id, status="active").update(status="seen")
            # print(response)
        
        passive_noti = list(notification.objects.filter(appntment_id__patient_id=patient_id).values('date_of_notification',
        'time_of_notification','changes_made','changes_made_by').order_by('-time_of_notification','-date_of_notification'))
        notice ={"active":active_noti,"passive":passive_noti}

    return JsonResponse(notice,safe= False)

#cancel of request
def cancelapp(request):
    if request.method =="POST":
        data= json.loads(request.body)
        patient_id=data['id']
        appointment.objects.filter(patient_id= patient_id).update(status="canceled")
        response = "canceled appointment"
    return JsonResponse(response, safe = False)

#name of the doctoo they visit often
def often(request):
    if request.method == "POST":
        data = json.loads(request.body)
        patient_id = data['id']
        data_list=list(appointment.objects.filter(patient_id=patient_id).values('doct_key_id__first_name',
        'doct_key_id__last_name').annotate(c=Count('doct_key_id')).order_by('-c'))
        data_=data_list[0]
        fname=data_['doct_key_id__first_name']
        lname=data_['doct_key_id__last_name']
        doctor={"fname":fname,"lname":lname}
    return JsonResponse(doctor, safe = False)


#all report
def all_report(request):
    if request.method =="POST":
        data= json.loads(request.body)
        patient_id=data['id']
        reports=list(report.objects.filter(appntment_id__patient_id= patient_id,).values('prescription', 'further_ins','date_of_report',
        'appntment_id__doct_key_id__first_name','appntment_id__doct_key_id__last_name','appntment_id__disease','time_of_report',
        'appntment_id__patient_id__first_name','appntment_id__patient_id__last_name','appntment_id__doct_key_id__department',
        ))
    return JsonResponse(reports, safe = False)

#for fetching all appointments
def all_appointments(request):
    if request.method == "POST":
        data=json.loads(request.body)
        patient_id = data['id'] 
        appointment_data=list(appointment.objects.filter(status_of_report="generated",patient_id=patient_id).values('id',
        'doct_key_id__first_name','doct_key_id__last_name','disease','date_for_app','time_for_app'))
    return JsonResponse(appointment_data,safe= False)


