from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True,verbose_name='ID Categoria')
    nombreCategoria=models.CharField(max_length=100,verbose_name='Nombre de Categoria')
    
class Imagen(models.Model):
    idImagen=models.AutoField(primary_key=True, verbose_name='ID Imagen')
    texto=models.CharField(max_length=120, verbose_name='Texto Descriptivo')
    nombreImagen=models.CharField(max_length=50, verbose_name='Nombre Imagen')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
