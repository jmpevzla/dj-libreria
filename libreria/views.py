from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return HttpResponse('<h1>Saludos desde la libreria</h1>')