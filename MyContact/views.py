from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm2, ContactForm3  # Assurez-vous d'importer votre formulaire
from .models import Contact  # Importer le modèle Contact
from django import forms

# Create your views here.
def controleform1(request):
    if request.method == 'POST':  # Correction de la syntaxe
        f = request.POST['firstname']  # firstname c'est le name dans la page HTML
        l = request.POST['lastname']
        e = request.POST['email']
        m = request.POST['message']

        # Création d'un nouvel objet Contact et sauvegarde
        contact = Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
        # contact.save() n'est pas nécessaire ici car create() sauvegarde automatiquement

        return HttpResponse('<h2> Data has been submitted </h2>')

    return render(request, "myform1.html")


def controleform2(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm2(request.POST)  # Nous reprenons les données

        if form.is_valid():  # Vérifie que les données envoyées sont valides
            # Ici, nous pouvons traiter les données du formulaire
            f = form.cleaned_data['firstname']
            l = form.cleaned_data['lastname']
            e = form.cleaned_data['email']  # Assurez-vous d'utiliser 'email' en minuscules
            m = form.cleaned_data['message']

            # Création d'un nouvel objet Contact et sauvegarde
            contact = Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
            return HttpResponse('<h2> Data has been submitted </h2>')
    else:
        # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm2()  # Crée une instance vide du formulaire

    return render(request, "myform2.html", {'mycontactform2': form})  # Passe le formulaire au template



def controleform3(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ContactForm3(request.POST)  # Nous reprenons les données
        
        if form.is_valid():  # Vérifie que les données envoyées sont valides
            form.save()  # Sauvegarde l'objet Contact
            return HttpResponse('<h2> Data has been submitted </h2>')
    else:
        # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm3()  # Crée une instance vide du formulaire

    return render(request, "myform3.html", {'mycontactform3': form})  # Passe le formulaire au template