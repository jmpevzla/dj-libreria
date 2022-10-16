from django.http import HttpResponse
from django.shortcuts import render
from .models import Libro
from .forms import LibroForm

# Create your views here.
TPL = 'libreria/'
TPL_PAGS = TPL +'paginas/'
TPL_LIBS = TPL + 'libros/'

def inicio(request):
    return render(request, TPL_PAGS + 'inicio.html')
def nosotros(request):
    return render(request, TPL_PAGS + 'nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, TPL_LIBS + 'index.html', { 'libros': libros })
def crear(request):
    formulario = LibroForm(request.POST or None)
    return render(request, TPL_LIBS + 'crear.html', { 'formulario': formulario })
def editar(request):
    return render(request, TPL_LIBS + 'editar.html')