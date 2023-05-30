from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return HttpResponse("Jetzt geht es aber")

def apfelbaum(request):
    return HttpResponse("Ja, das ist ein Apfelbaum")

def apfelbaum_n(request, name, number):
    antwort = f"Gute Tag {name}. Sie haben die Zahl {number} übergeben."
    return HttpResponse(antwort)

def mutter(request, id):
    ds = Mutter.objects.filter(id=id)
    if len(ds)==1:
        #ds = Mutter.objects.get(id=id)
        return HttpResponse(ds[0])
    else:
        return HttpResponse("Ach komm, die Mutter gib es garnicht")

    
