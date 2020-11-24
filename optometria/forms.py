from django import forms
from django.forms import ModelForm, DateField
from .models import Turno, Hc

class TurnoForm(ModelForm):
    fecha = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control'}))
    class Meta:
        model = Turno
        fields = '__all__'


class HcForm(ModelForm):
    fecha = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control'}))
    class Meta:
        model = Hc
        fields = '__all__'
