from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import teachers
from django.core import serializers

def validate(request):
    email=request.GET['email']
    pas=request.GET['pas']
    try:
        obj=teachers.objects.get(email=email)
        if obj.pas==pas:
            return JsonResponse({'status':True})
        else:
            return JsonResponse({'status':False})
    except:
        return JsonResponse({'status':False})

def data(request):
    obj=teachers.objects.all()
    data=serializers.serialize('json',obj,fields=('pk','email','pas'))
    return JsonResponse(data,safe=False)

def postValidate(request):
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['pas']
        print(email,pas)
        try:
            obj=teachers.objects.get(email=email)
            if obj.pas==pas:
                return JsonResponse({'status':True})
            else:
                return JsonResponse({'status':False})
        except:
            return JsonResponse({'status':False})
    return HttpResponse("hello")

def test(request):
    return JsonResponse([{'email':'atul'},
    {'email':'rahul'}],safe=False)
