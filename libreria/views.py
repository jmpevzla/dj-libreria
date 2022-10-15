from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
TPL = 'libreria/'
TPL_PAGS = TPL +'paginas/'

def inicio(request):
    return HttpResponse('<h1>Saludos desde la libreria</h1>')
def nosotros(request):
    return render(request, TPL_PAGS + 'nosotros.html')