from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import PatientForm, DoctorForm, DonorForm, HospitalRegForm ,addServiceForm,bookServiceForm,AskQuesForm,AnswerForm
from django.contrib.auth import authenticate,login
from django.db import models
from .models import Services,Questions,Answer,Donor,Hospital
from django.contrib.auth import logout



#from .models import Doctor,Patient,Questions

# Create your views here.

def home(request):
    return render(request,'app1/home.html')

def signup(request):
    return render(request,'app1/signup.html')


def patient(request):
    if request.method=="POST":
        form1= UserCreationForm(request.POST)
        form2=PatientForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            var1=form1.save()
            var2=form2.save(commit=False)
            var2.user=var1
            var2.save()
            var1=authenticate(username=var1.username, password=form1.cleaned_data.get('password1'))
            login(request,var1)
            return redirect ('app1:home')
    else:
        form1 = UserCreationForm
        form2= PatientForm()
    return render(request,'app1/patient.html',{'form1':form1,'form2':form2})

def doctor(request):
    if request.method=="POST":
        form1= UserCreationForm(request.POST)
        form2=DoctorForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            var1=form1.save()
            var2=form2.save(commit=False)
            var2.user=var1
            var2.save()
            var1=authenticate(username=var1.username, password=form1.cleaned_data.get('password1'))
            login(request,var1)
            return redirect ('app1:home')
            
    else:
        form1 = UserCreationForm
        form2= DoctorForm()
    return render(request,'app1/doctor.html',{'form1':form1,'form2':form2})

def donor(request):
    if request.method=="POST":
        form1= UserCreationForm(request.POST)
        form2=DonorForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            var1=form1.save()
            var2=form2.save(commit=False)
            var2.user=var1
            var2.save()
            var1=authenticate(username=var1.username, password=form1.cleaned_data.get('password1'))
            login(request,var1)
            return redirect ('app1:home')
    else:
        form1 = UserCreationForm
        form2= DonorForm()
    return render(request,'app1/donor.html',{'form1':form1,'form2':form2})

def hospitalReg(request):
    if request.method=="POST":
        form1= UserCreationForm(request.POST)
        form2=HospitalRegForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            var1=form1.save()
            var2=form2.save(commit=False)
            var2.user=var1
            var2.save()
            var1=authenticate(username=var1.username, password=form1.cleaned_data.get('password1'))
            login(request,var1)
            return redirect ('app1:home')
    else:
        form1 = UserCreationForm
        form2= HospitalRegForm()

    return render(request,'app1/hospitalReg.html',{'form1':form1,'form2':form2})

def user_show(request):
    return render(request,'app1/usershow.html')


def questions(request):
    if request.method=="POST":
        form=AskQuesForm(request.POST)
        var2=form.save(commit=False)
        var2.patient=request.user.patient
        #var2.patient=(Patient.objects.get(user=x)).user
        var2.save()
        return redirect ('app1:home')
    else:
        form= AskQuesForm()
    return render(request,'app1/askques.html',{'form':form})

from django.db.models import Q

def viewQues(request):
    ques = Questions.objects.all()
    ans = Answer.objects.all()
    search_query = request.GET.get('search')

    if search_query:
        ques = ques.filter(Q(question__icontains=search_query))

    form = AnswerForm(request.POST)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        questionId = request.POST.get('questionId')
        var1 = form.save(commit=False)
        var1.doctor = request.user.doctor
        var1.question = Questions.objects.get(pk=questionId)
        var1.save()
        return redirect('app1:viewques')
    else:
        form = AnswerForm()
    
    return render(request, "app1/viewques.html", {'questions': ques, 'answers': ans})


def addService(request):
    if request.method=="POST":
      form=addServiceForm(request.POST)
      var1=form.save(commit=False)
      var1.user=request.user.hospital
      var1.save()
      return redirect ('app1:home')
    else:
        form=addServiceForm()
    return render(request,'app1/addService.html',{'form':form})

"""
def bookService(request):
    services=Services.objects.all()
    hospital=Hospital.objects.all()
    if request.method=="POST":
      form=bookServiceForm(request.POST)
      if form.is_valid():
        var1=form.save(commit=False)
        var1.patient = request.user.patient
        #print(request.user.patient)
        if Services.objects.filter(user_id=var1.hospital, id=var1.serviceType_id).update(availability=models.F('availability') - 1):
           var1.save()
           return redirect ('app1:done')
        else:
            return redirect ('app1:sorry')
    else:
        form=bookServiceForm()
    return render(request,'app1/bookService.html',{'form':form,"services":services,"hospitals":hospital})
"""

def bookService(request):
    services=Services.objects.all()
    return render(request,'app1/bookService.html',{"services":services})

def booking(request,id):
    Services.objects.filter(id=id).update(availability=models.F('availability') - 1)
    #services.availability=services.availability-1
    return redirect ('app1:done')


def donorview(request):
    donors=Donor.objects.all()
    return render(request,"app1/donorview.html",{"donors":donors})


def done(request):
     return render(request,"app1/done.html")


def sorry(request):
     return render(request,"app1/sorry.html")

def logout_view(request):
    logout(request)
    return redirect ('app1:home')

