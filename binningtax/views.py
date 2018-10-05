from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
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
    if request.method == 'POST':
        form_contact = request.POST
        message = "Subject: " + form_contact['subject']
        message += "\n Body: " + form_contact['body']
        message += "\n\n\nFrom: "
        message += "\n" + form_contact['fname'] + " "
        message += form_contact['lname']
        message += "\nEmail address "
        message += form_contact['email']
        message += "\nPhone: " + form_contact['phone']

        send_mail(
            'Web Query',
            message,
            'query@binningconsultants.com',
            ['info@binningconsultants.com'],
            fail_silently=False,
        )
        print(form_contact['fname'])
    form = ContactForm()
    return render(request, 'binningtax/contact.html', {'form': form})
