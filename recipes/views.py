from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HOME")


def contato(request):
    return HttpResponse("Contato")

def sobre(request):
    return HttpResponse("Sobre")