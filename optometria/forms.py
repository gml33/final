from django import forms
from .models import *

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'


class HcForm(forms.ModelForm):
    class Meta:
        model = Hc
        fields = '__all__'
        

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class LenteForm(forms.ModelForm):
    class Meta:
        model = Lente
        fields = '__all__'
