from django import forms


class ContactForm(forms.Form):
    fname = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First name',
            'required': 'true',
        }
    ))

    lname = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last name',
            'required': 'true',
        }
    ))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter email here',
            'required': 'true',
        }
    ))
    phone = forms.CharField(label='Phone', widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': '1-(555)-555-5555',
            'required': 'true',
        }
    ))
    subject = forms.CharField(required=False, label='Subject', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))
    body = forms.CharField(label='Question', widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows': 3,
            'required': 'true',
        }
    ))
