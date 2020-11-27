from django.shortcuts import render, redirect, reverse
from .utils import *
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from datetime import datetime


User = get_user_model()


def index(request):
    return render(request, 'optometria/index.html',{
        'grupo': request.user.rol
    })
#----------------------------------------------turnos----------------------------------------------
def ver_turnos(request):
    if len(Turno.objects.all()) > 0:
        data = Turno.objects.all()
    else:
        data = None
    return render(request, 'optometria/ver_turno.html',{
        'grupo': request.user.rol,
        'data': data,
        })

def agregar_turno(request):    
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            paciente = form.cleaned_data['paciente']
            cumplio = form.cleaned_data['cumplio']
            medico = form.cleaned_data['medico']
            form.save()
            messages.success(request, ('El turno fue creado exitosamente.'))
            return HttpResponseRedirect(reverse('optometria:ver_turnos'))
    else:
        form = TurnoForm()        
    return render(request, 'optometria/agregar_turno.html',{
        'grupo': request.user.rol,
        'pacientes':User.objects.filter(rol='paciente'),
        'medicos':User.objects.filter(rol='medicos'),
        })

def editar_turno(request, id):
    turno = Turno.objects.get(id=id)
    if request.user.rol == 'secretario':
        if request.method == 'GET':
            form = TurnoForm(instance=turno)
        else:
            form = TurnoForm(request.POST, instance= turno)
            if form.is_valid():
                form.save()
                messages.success(request, ('El turno fue editado exitosamente.'))
                return HttpResponseRedirect(reverse('optometria:ver_turnos'))
    else:
        form = TurnoForm()
    return render(request, 'optometria/editar_turno.html',{
        'grupo': request.user.rol,
        'pacientes':User.objects.filter(rol='paciente'),
        'medicos':User.objects.filter(rol='medicos'),
        })


def eliminar_turno(request, id):
    data = Turno.objects.all()
    turno = Turno.objects.get(id=id)
    if request.user.rol == 'secretario':
        turno.delete()
        messages.success(request, ('El turno fue eliminado exitosamente.'))
        return render(request, 'optometria/ver_turno.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    else:
        messages.success(request, ('Ocurrió un error, por favor intente nuevamente'))
        return render(request, 'optometria/ver_turno.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    return render(request, 'optometria/ver_turno.html',{
            'grupo': request.user.rol,
            'data': data,
        })
#--------------------------------------------------------HC--------------------------------------------
def ver_hc(request):
    if len(Hc.objects.all()) > 0:
        data = Hc.objects.filter(medico_id = request.user.id)
    else:
        data = None
    return render(request, 'optometria/ver_hc.html',{
        'grupo': request.user.rol,
        'data': data,
        })


def agregar_hc(request):    
    if request.method == 'POST':
        form = HcForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            paciente = form.cleaned_data['paciente']
            detalle = form.cleaned_data['detalle']
            medico = form.cleaned_data['medico']
            form.save()
            messages.success(request, ('Hc fue creado exitosamente.'))
            return HttpResponseRedirect(reverse('optometria:ver_hc'))
        else:
            form = HcForm()
    return render(request, 'optometria/agregar_hc.html',{
        'grupo': request.user.rol,
        'pacientes':User.objects.filter(rol='paciente'),
        'medico':request.user.id
        })


def editar_hc(request, id):
    hc = Hc.objects.get(id=id)
    if request.user.rol == 'medicos':
        if request.method == 'GET':
            form = HcForm(instance=hc)
        else:
            form = HcForm(request.POST, instance=hc)
            if form.is_valid():
                form.save()
                messages.success(request, ('La Historia clínica fue editada con exito, fuck yeahh!!!!!.'))
                return HttpResponseRedirect(reverse('optometria:ver_hc'))
    else:
        form = HcForm()
    return render(request, 'optometria/editar_hc.html',{
        'grupo': request.user.rol,
        'pacientes':User.objects.filter(rol='paciente'),
        'medicos':User.objects.filter(rol='medicos'),
        })


def eliminar_hc(request, id):
    data = Hc.objects.filter(medico_id = request.user.id)
    hc = Hc.objects.get(id=id)
    if request.user.rol == 'medicos':
        hc.delete()
        messages.success(request, ('Se eliminó la Historia clínica.'))
        return render(request, 'optometria/ver_hc.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    else:
        messages.success(request, ('Ocurrió un error, estamos en la sopa..... :('))
        return render(request, 'optometria/ver_hc.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    return render(request, 'optometria/ver_hc.html',{
            'grupo': request.user.rol,
            'data': data,
        })
#-------------------------------------------productos----------------------------------------------
