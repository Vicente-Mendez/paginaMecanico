from django.forms import ModelForm
from main.models import Imagen


class ImagenForm(ModelForm):
    class Meta:
        model = Imagen
        fields = '__all__'
 