from django.shortcuts import render
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
def signup(request):
    return render(request,'signup.html')
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
    return render(request,'for_service.html',{"users":user})

def submit(request):
    name1 = request.POST["s_name"]
    print(name1)
    return HttpResponse(name1)
# def signup(request):
#     mail = request.POST["Signup"]
#     obj = models.email()
    
#     obj.EMAIL = mail
#     obj.save()
#     return render(request,'home.html')
    
    
