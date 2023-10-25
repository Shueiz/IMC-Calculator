from django.shortcuts import render, redirect
from .models import IMCResult

def calculate_imc(request):
    result = 0
    if request.method == 'POST':
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        result = round(weight / (height ** 2), 2)
        IMCResult.objects.create(height=height, weight=weight, result=result)
    return render(request, 'imc/calculate_imc.html',{'result' : result})

def view_results(request):
    results = IMCResult.objects.order_by('-timestamp')[:5]
    return render(request, 'imc/view_results.html', {'results': results})

def home(request):
    return redirect(calculate_imc)

