from django.shortcuts import render,redirect
from . models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy 
from clinicalApp.forms import ClinicalDataForm
# Create your views here.

class PatientListView(ListView):
    model= Patient

class PatientCreateView(CreateView):
    model= Patient
    success_url= reverse_lazy('index')
    fields=('first_name','last_name','age')

class PatientUpdateView(UpdateView):
    model= Patient
    success_url= reverse_lazy('index')
    fields=('first_name','last_name','age')

class PatientDeleteView(DeleteView):
    model= Patient
    success_url= reverse_lazy('index')

def addData(request,**id):
    form = ClinicalDataForm()
    patient= Patient.objects.get(id=id['pk']) #to get single patient data

    if request.method=='POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalApp/clinicaldata_from.html',{'form':form,'patient':patient})

def analyze(request,**kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData=[]
    for eachEntry in data:
        if eachEntry.componentName =='HW':
            heightAndWeight= eachEntry.componentValue.split('/')
            if len(heightAndWeight) > 1:
                meters = float(heightAndWeight[0])*0.4536 
                bmi = (float(heightAndWeight[1]))/(meters*meters)
                bmiEntry= ClinicalData()
                bmiEntry.componentName='BMI'
                bmiEntry.componentValue=bmi 
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request,'clinicalApp/generateReport.html',{'data':responseData})
