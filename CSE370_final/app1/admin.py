from django.contrib import admin
from . models import Patient, Doctor, Donor, Hospital


# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Donor)
admin.site.register(Hospital)

