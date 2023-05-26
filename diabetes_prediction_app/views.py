import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load
from django.http import request
from django.shortcuts import render
from django.contrib import messages


model = load('./MLmodel/model.joblib')

def home(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        age = request.POST['age']
        hypertension = request.POST['hypertension']
        heart_disease = request.POST['heart_disease']
        smoking_history = request.POST['smoking_history']
        bmi = request.POST['bmi']
        HbA1c_level = request.POST['HbA1c_level']
        blood_glucose_level = request.POST['blood_glucose_level']
        y_pred = model.predict(
            [[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]])
        if y_pred[0] == 0:
            y_pred = 'Diabetes result is Negative'

        else:
            y_pred = 'Diabetes result is Positive'
        return render(request, 'home.html', {'result': y_pred})
    return render(request, 'home.html')




