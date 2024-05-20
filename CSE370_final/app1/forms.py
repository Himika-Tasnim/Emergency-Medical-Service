from django import forms
from . models import Patient,Doctor,Donor,Hospital,Services,Booking,Questions,Answer

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['name','email','gender','bloodGroup','age']


class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['name','email','bmNum','specialization']

class DonorForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields=['name','email','gender','bloodGroup','lastDonation','isSmoker','location']

class AskQuesForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=["question"]

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=["answer"]


class HospitalRegForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields=["name","regNum","hotline","location","speciality"]

class addServiceForm(forms.ModelForm):
    class Meta:
        model=Services
        fields=["type","availability","costRange"]

class bookServiceForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=[]
        #fields=["hospital","serviceType"]

