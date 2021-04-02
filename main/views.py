from django.shortcuts import render
from . import models
from .filters import GaleriaFiltro
# Create your views here.

def Index(request):
    imagenes=models.Imagen.objects.all()
    datos={"imagenes":imagenes}
    return render(request, 'index.html',datos)

def InfoCategoria(request):
    categorias=models.Categoria.objects.all()
    datos={"categorias":categorias}
    return render(request, 'infocategorias.html',datos)

def verImagen(request, id):
    imagen=models.Imagen.objects.get(idImagen=id)
    datos={"imagen":imagen}
    return render(request, 'verImagen.html', datos)


def galeriaMecanico(request):
    context = {}

    imagenes_filtro = GaleriaFiltro(
        request.GET,
        queryset=models.Imagen.objects.all()
    )

    context['imagenes_filtro'] = imagenes_filtro

    return render(request,'galeriaMecanico.html',context=context)