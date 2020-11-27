from django import forms
from django.forms import ModelForm, DateField, DateTimeInput
from .models import *

class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'


class HcForm(ModelForm):
    class Meta:
        model = Hc
        fields = '__all__'
        

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
