from django import forms
from django.forms import ModelForm

from MyContact.models import Contact

class ContactForm2(forms.Form):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    email = forms.EmailField()  # Remarquez que j'ai changé 'Email' en 'email'
    message = forms.CharField(widget=forms.Textarea)

class ContactForm3(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'message']  