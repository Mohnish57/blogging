from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Myform
from django.contrib import messages
from .models import data, content

def signup(req):
   return render(req,"signup.html")
def signuptask(req):
    ob=data()
    ob.name=req.POST.get("name")
    ob.email=req.POST.get("email")
    ob.gender=req.POST.get("gender")
    ob.dob=req.POST.get("dob")
    ob.mobile=req.POST.get("mobile")
    ob.password=req.POST.get("password")
    ob.save() 
    return redirect("/login")
 
def login(req):
    if req.method=="POST":
      form=Myform(req.POST)
      if form.is_valid():
         messages.success(req,"Success!")
         return redirect("/logintask")
      else:
         messages.error(req,"Wrong Captcha!")
    form=Myform()
    return render(req,"login.html",{"form":form})
global email  
def logintask(req):
    global email
    email=req.POST.get("email")
    password=req.POST.get("password")
    form=Myform(req.POST)
    if form.is_valid():
        Data=data.objects.filter(email=email,password=password)
        form=Myform()
        if Data.exists():
            f=data.objects.filter(email=email)
            Post=content.objects.all()
            
            return render(req,"dashboard.html",{"data":f,"Post":Post})
        else:
            g="No such user found"
            form=Myform()
            return render(req,"login.html",{"span":g})
    else:
        c="Captcha not matched!!"
        return render(req,'login.html',{'form':form,'c':c})
def dashboard(req):
    Data=data.objects.all()
    Post=content.objects.all()
    return render(req,'dashboard.html',{"Data":Data,"Post":Post})
def post(req):
    ob=content()
    ob.name=req.POST.get("name")
    ob.email=req.POST.get("email")
    ob.title=req.POST.get("title")
    ob.content=req.POST.get("content")
    ob.save()
    return redirect("/dashboard")

def editprofile(req):
	rec=data.objects.filter(email=email)
	return render(req,"editprofile.html",{"list":rec})
	
def updatetask(req):
    ID=req.POST.get("ID")
    oc=data.objects.get(id=ID)
    oc.name=req.POST.get("name")
    oc.email=req.POST.get("email")
    oc.mobile=req.POST.get("mobile")
    oc.dob=req.POST.get("dob")
    oc.password=req.POST.get("password")
    oc.save() 
    return redirect("/dashboard")

def dashboard(req):
    Data=data.objects.all()
    Post=content.objects.all()
    return render(req,'dashboard.html',{"Data":Data,"Post":Post})
def profile(req):
    Data=data.objects.filter(email=email)
    for i in Data:
        Name=i.name
        Email=i.email
    Post=content.objects.all()
    return render(req,'profile.html',{"data":Data,"name":Name,"email":Email})