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

def familie(request):
    liste_kinder = Kind.objects.all()
    contents = {
        'liste': liste_kinder,
        'vors': 'kind',
        'h1': 'Liste der Kinder',
    }
    return render(request, 'app1/liste.html', contents)

def muetter(request):
    liste = Mutter.objects.all()
    contents = {
        'liste': liste,
        'vors': 'mutter',
        'h1': 'Liste der Mütter',
    }
    return render(request, 'app1/liste.html', contents)
    
def kind_detail(request, name):
    kind = Kind.objects.get(pk=name)
    contents = {
        'kind': kind,
    }
    return render(request, 'app1/kind_detail.html', contents)
    
