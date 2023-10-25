
from django.contrib import admin
from django.urls import path
from imc import views

urlpatterns = [
    path('calculate_imc/', views.calculate_imc, name='calculate_imc'),
    path('view_results/', views.view_results, name='view_results'),
    path('', views.home, name='home'),
]
