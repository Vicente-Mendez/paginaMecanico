from main.models import Categoria
from rest_framework import viewsets
from .serializer import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all()
    serializer_class=CategoriaSerializer