from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    gender=models.CharField(max_length=25)
    bloodGroup = models.CharField(max_length=10)
    age=models.IntegerField()

class Donor(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    gender=models.CharField(max_length=25)
    bloodGroup = models.CharField(max_length=10)
    lastDonation=models.DateField(null=False)
    isSmoker=models.BooleanField()
    location=models.CharField(max_length=100)

class Doctor(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    bmNum=models.IntegerField()
    specialization=models.CharField(max_length=255)


class Questions(models.Model):
    id = models.AutoField(primary_key=True)  
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    question=models.CharField(max_length=255)

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=255,null=True)


class Hospital(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name=models.CharField(unique=True,max_length=255)
    regNum=models.IntegerField(unique=True)
    hotline=models.IntegerField()
    location=models.CharField(max_length=255)
    speciality=models.CharField(max_length=255)
    def __str__(self):
      return self.name

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    type=models.CharField(max_length=50)
    availability=models.IntegerField()
    costRange=models.CharField(max_length=100)
    class Meta:
        unique_together= ("user","type")
    def __str__(self):
      return f"{self.user}:{self.type}"

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name="hospital")
    serviceType=models.ForeignKey(Services,on_delete=models.CASCADE,related_name="service")
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)

