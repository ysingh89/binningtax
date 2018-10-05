from django import forms


class ContactForm(forms.Form):
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')
    email = forms.EmailField(label='E-mail')
    phone = forms.CharField(label='Phone')
    subject = forms.CharField(required=False, label='Subject')
    body = forms.CharField(widget=forms.Textarea, label='Question')
