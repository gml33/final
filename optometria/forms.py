from django import forms
from django.forms import ModelForm, DateField, DateTimeInput
from .models import Turno, Hc

class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'


class HcForm(ModelForm):
    class Meta:
        model = Hc
        fields = '__all__'
