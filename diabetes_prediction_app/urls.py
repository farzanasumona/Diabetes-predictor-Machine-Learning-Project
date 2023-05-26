from django.contrib import admin
from django.urls import path
from diabetes_prediction_app import views

urlpatterns = [
    path('', views.home, name='view')

]
