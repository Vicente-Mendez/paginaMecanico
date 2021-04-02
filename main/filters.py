import django_filters

from .models import Imagen

class GaleriaFiltro(django_filters.FilterSet):
    class Meta:
        model = Imagen
        fields = ['categoria']