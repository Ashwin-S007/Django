from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse,HttpResponseRedirect
from .models import DiabetesInput
from .forms import Diabetes_form
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from diabetes_GB.backend import trainModel,predictData
from csv import writer
# reading csv file and extracting class column to y.
L=[]
prediction=""

def home(request):
    return render(request, 'home_GB.html')


def index(request):
    return render(request, 'index_GB.html')

def predict_diabetes(request):
    global prediction,L
    L=[]
    prediction=""
    if request.method == 'POST':
        glucose_str = request.POST.get('glucose', '')
        blood_pressure_str = request.POST.get('blood_pressure', '')
        bmi_str = request.POST.get('bmi', '')
        insulin_str = request.POST.get('insulin','')
        skinthickness_str = request.POST.get('skin_thickness','')
        pregnancies_str = request.POST.get('pregnancy','')
        age_str = request.POST.get('age','')
        diabetespedigree_str = request.POST.get('diabetes_pedigree','')


        # Check if any of the fields are empty
        if not glucose_str or not blood_pressure_str or not bmi_str:
            return render(request, 'index_GB.html', {'error': 'Please fill in all fields.'})

        glucose = float(glucose_str)
        blood_pressure = float(blood_pressure_str)
        bmi = float(bmi_str)
        insulin = float(insulin_str)
        skinthickness = float(skinthickness_str)
        pregnancies = float(pregnancies_str)
        age = float(age_str)
        diabetespedigree = float(diabetespedigree_str)
        # Simple rule-based prediction for demonstration
        L=[pregnancies,glucose,blood_pressure,skinthickness,insulin,bmi,diabetespedigree,age]
        predict = predictData(L)
        if(predict == 0):
            prediction="No Diabetes"
        else:
            prediction="Possible Diabetes"
        data = DiabetesInput(glucose=glucose,blood_pressure=blood_pressure,bmi=bmi,insulin=insulin,skinthickness=skinthickness,pregnancies=pregnancies,Age=age,DiabetesPedigree=diabetespedigree,Prediction=prediction)
        data.save()
        return render(request, 'result_GB.html', {'prediction': prediction})

    return render(request, 'index_GB.html')

def history(request):
    db=DiabetesInput.objects.all()
    return render(request, 'history_GB.html', {"db":db})
def update(request):
    L=DiabetesInput.objects.all().last()
    
    predict = request.GET["Prediction"]
    feedback = request.GET["review"]
    if predict == "Yes":
        p = (1 if(L.Prediction == "Possible Diabetes") else 0)
    else:
        p = 0 if L.Prediction == "Possible Diabetes" else 1
    new_record=[[L.pregnancies,L.glucose,L.blood_pressure,L.skinthickness,L.insulin,L.bmi,L.DiabetesPedigree,L.Age,p]]
    df = pd.DataFrame(new_record)
 
    # append data frame to CSV file
    df.to_csv("C:/MINI-PROJ/diabetes_prediction/org_data.csv", mode='a', index=False, header=False,sep=",")
    return render(request, 'home_GB.html')

    

