from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)

class ClinicalData(models.Model):
    COMPONENT_NAMES=[('HW','Height/Weight'),('BP','Blood Pressure'),('heartrate','Heart Rate')]
    componentName=models.CharField(choices=COMPONENT_NAMES,max_length=20)
    componentValue=models.CharField(max_length=20)
    measuredDateTime= models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)