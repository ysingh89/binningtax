from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'binningtax/home.html')


def tax(request):
    return render(request, 'binningtax/tax.html')
    # return HttpResponse("Hello from tax page")

def immigration(request):
    return render(request, 'binningtax/immigration.html')