from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos de nous</h1><p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listing</h1><p>Afficher ici la liste des produits</p>')

def contact(request):
    return HttpResponse('<h1>Contact</h1><p>Afficher les coordonnées de contact</p>')
