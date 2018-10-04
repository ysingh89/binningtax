from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.


def home(request):
    return render(request, 'binningtax/home.html')


def tax(request):
    return render(request, 'binningtax/tax.html')
    # return HttpResponse("Hello from tax page")


def immigration(request):
    return render(request, 'binningtax/immigration.html')


def indian(request):
    return render(request, 'binningtax/indian.html')


def contact(request):
    form = ContactForm()
    return render(request, 'binningtax/contact.html', {'form': form})
