from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea, label='Query')
