from django.shortcuts import render, redirect
from django.http import HttpResponse
from New_way import models
# Create your views here.
def New_way(request):
    return render(request,'home.html')
def home(request):
    return render(request,'home.html')
def employe(request):
    return render(request,'employe.html')
def user(request):
    return render(request,'user.html')


    
def login(request):
    return render(request,'user.html')
def register(request):
    return render(request,'Job_hiring.html')
def job_hiring(request):
    return render(request, 'Job_hiring.html')
# def register(request):
#     return render(request,'Register.html')
def services(request):
    return render(request,'services.html')
def pro(request,user):
    return render(request,'for_service.html',{'users':user})

def submit(request):
    obj = models.hiring()
    obj.name = request.POST["s_name"]
    obj.location = request.POST["address"]
    obj.contactno = request.POST["conno"]
    obj.mail = request.POST["email"]
    obj.qualification = request.POST["qualification"]
    obj.jobrole = request.POST["job"]
    obj.experience = request.POST["experience"]
    obj.save()
    return HttpResponse("<h1>login sucessfully</h1>")
    
    
# def signup(request):
#     mail = request.POST["Signup"]
#     obj = models.email()
    
#     obj.EMAIL = mail
#     obj.save()
#     return render(request,'home.html')

def sign(request):
    if request.method == 'POST':
        obj = models.signup()
        obj.username = request.POST["name"]
        obj.email = request.POST["email"]
        obj.password = request.POST["password"]
        obj.save()
        return render(request,"services.html")
    else:
        return render(request,'signup.html')
    

def book(request):

    if request.method == 'POST':
        obj = models.services()
        obj.service_required_on = request.POST["frdate"]
        obj.service_required_at = request.POST["fraddress"]
        obj.contact = request.POST["frcno"]
        obj.mail = request.POST["fremail"]
        obj.information = request.POST["fraddinf"]
        obj.save()
        return render(request, "result.html")
    else:
        return render(request, 'for_service.html')

    
    
