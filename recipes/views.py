from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/index.html')


def contato(request):
    return HttpResponse("Contato")

def sobre(request):
    return HttpResponse("Sobre")