from django.shortcuts import render, redirect
from main import models
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ImagenForm

# Create your views here.
@login_required
def SubirImagen(request):
    categorias=models.Categoria.objects.all()
    datos={"categorias":categorias}
    return render(request, 'subirImagen.html', datos)

def GuardarImagen(request):
    if request.method=='POST':
        imagen=request.FILES['imagen']
        idImagen=request.POST['idImagen']
        texto=request.POST['texto']
        nombreImagen=imagen.name
        categoria=request.POST['categoria']

        #guardar el archivo en el directorio
        arch=FileSystemStorage()

        arch.save(imagen.name, imagen)

        #sacamos la categoria desde la BD
        c=models.Categoria.objects.get(idCategoria=categoria)
        #Guarda los datos en la BD
        cate=models.Imagen(idImagen=idImagen, texto=texto, nombreImagen=nombreImagen, categoria=c)
            
        cate.save()
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/subirImagen/')

@login_required
def ModificarImagen(request, pk):

    imagen = models.Imagen.objects.get(idImagen=pk)
    form = ImagenForm(instance=imagen)

    if request.method == 'POST':
        form = ImagenForm(request.POST, instance = imagen)
        if form.is_valid():
            form.save()
            return redirect('/index')

    datos = {'form':form}
    return render(request, "modificarImagen.html", datos)

@login_required
def EliminarImagen(request, pk):
    imagen = models.Imagen.objects.get(idImagen=pk)
    if request.method == 'POST':
        imagen.delete()
        return redirect('/index')
        
    datos = {'item':imagen}
    return render (request, "eliminarImagen.html", datos )




def registro(request):

    form = UserCreationForm()

    if request.method == "POST":

        form = UserCreationForm(data=request.POST)

        if form.is_valid():

            user = form.save()

            if user is not None:

                do_login(request, user)

                return redirect('/index')


    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "registro.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            do_login(request, user)
            return redirect('/index')
    return render(request, "login.html", {'form': form})  

def logout(request):
    do_logout(request)
    return redirect('/index')

