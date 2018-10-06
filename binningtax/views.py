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
    form = ContactForm()
    if request.method == 'POST':
        form_contact = request.POST
        # print(form_contact)
        message = "Subject: " + form_contact['subject']
        message += "\nBody: " + form_contact['body']
        message += "\n\n\nFrom: "
        message += "\n" + form_contact['fname'] + " "
        message += form_contact['lname']
        message += "\nEmail address: "
        message += form_contact['email']
        message += "\nPhone: " + form_contact['phone']

        try:
            send_mail(
                'Web Query',
                message,
                'query@binningconsultants.com',
                ['info@binningconsultants.com'],
                fail_silently=False,
            )
        except Exception as e:
            pass
        else:
            return render(request,
                          'binningtax/contact.html',
                          {'form': form, 'message': 'Your query has been submitted successfully.'})

        # print(form_contact['fname'])
    return render(request, 'binningtax/contact.html', {'form': form})
