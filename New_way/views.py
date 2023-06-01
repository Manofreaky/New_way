from django.shortcuts import render, redirect
from django.http import HttpResponse
from New_way import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from django.http import HttpResponse
from New_way.models import signup
# email
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
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

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            udata = User.objects.get(email=email)
            username = udata.username
            print(username)
            authuser = authenticate(request, username=username, password=password)
            if authuser is not None:
                auth_login(request, authuser)
                return redirect('home')
            else:
                error = "Invalid Data"
        except:
            error = "User not found"
    else:
        error = ""

    return render(request, 'user.html', {'error': error})

def logouts(request):
    logout(request)
    return redirect('home')
def job_hiring(request):
    if request.method == 'POST':
        obj = models.hiring()
        obj.name = request.POST['ename']
        obj.password = request.POST['epass']
        obj.location = request.POST['eaddress']
        obj.contactno = request.POST['econno']
        obj.mail = request.POST['eemail']
        obj.qualification = request.POST['equalification']
        obj.jobrole = request.POST['ejob']
        obj.experience = request.POST['eexperience']
        obj.save()
        print('!!!!!!!!!!!!!!')
        return render(request,"employeeresult.html")
    else:
        return render(request,'Job_hiring.html')
# def register(request):
#     return render(request,'Register.html')
# def services(request):
#     return render(request,'services.html')



def sign(request):
    error=""
    if request.method == 'POST':
        obj = models.signup()
        obj.username = request.POST['signname']
        obj.email = request.POST['signemail']
        obj.password = request.POST['signpassword']
        print('!!!!!!!!!!!!')
        if User.objects.filter(email=obj.email).exists():
            error="email already exists"
        else:
            user=User.objects.create_user(username=obj.username,email=obj.email,password=obj.password)
            user.save()
            obj.save()
            return redirect('login')
    
    return render(request,'signup.html',{'error':error})
    

def book(request):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if request.method == 'POST':
        obj = models.services()
        obj.service_for = request.POST['fname']
        obj.service_required_on = request.POST["frdate"]
        obj.service_required_at = request.POST["fraddress"]
        obj.contact = request.POST["frcno"]
        obj.mail = request.POST["fremail"]
        obj.information = request.POST["fraddinf"]
        data = {
            "name": obj.service_for,
            "date": obj.service_required_on,
            "address": obj.service_required_at,
            "contact": obj.contact,
            "email": obj.mail,
            "additional_information": obj.information
        }
        send_mail("college", str(data), 'your_email@gmail.com', [obj.mail])
        obj.save()
        return render(request,'result.html')
    else:
        return render(request, 'for_service.html')

    
    
