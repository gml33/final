from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .utils import *
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages



def grupo(request):
    if str(request.user.groups.all().first()) == 'Paciente':
        grupo = 'paciente'
    elif str(request.user.groups.all().first()) == 'gerencia':
        grupo = 'gerencia'
    elif str(request.user.groups.all().first()) == 'medicos':
        grupo = 'medicos'
    elif str(request.user.groups.all().first()) == 'secretario':
        grupo = 'secretario'
    elif str(request.user.groups.all().first()) == 'taller':
        grupo = 'taller'
    elif str(request.user.groups.all().first()) == 'venta':
        grupo = 'venta'
    else:
        grupo = 'grupo no definido'
    return grupo



def index(request):
    grupo_usuario = grupo(request)
    return render(request, 'optometria/index.html',{
        'grupo': grupo_usuario
    })
#----------------------------------------------turnos----------------------------------------------
def ver_turnos(request):
    grupo_usuario = grupo(request)
    data = Turno.objects.all()
    return render(request, 'optometria/ver_turno.html',{
        'grupo': grupo_usuario,
        'data': data,
        })

def agregar_turno(request):
    grupo_usuario = grupo(request)
    form = TurnoForm
    if request.method == 'POST':
        form = TurnoForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.cumplio = False
            form.save()
            messages.success(request, ('El turno fue agregado exitosamente.'))
            grupo_usuario = grupo(request)
            data = Turno.objects.all()
            return render(request, 'optometria/ver_turno.html',{
                'grupo': grupo_usuario,
                'data': data,
            })
        else:
            messages.success(request, ('Ocurrió un error, por favor intente nuevamente'))
            return render(request, 'optometria/agregar_turno.html',{'formulario':form})
    else:
        return render(request, 'optometria/agregar_turno.html',{'formulario':form})


def eliminar_turno(request, id):
    grupo_usuario = grupo(request)
    data = Turno.objects.all()
    turno = Turno.objects.get(id=id)
    if grupo_usuario == 'secretario':
        turno.delete()
        messages.success(request, ('El turno fue eliminado exitosamente.'))
        return render(request, 'optometria/ver_turno.html',{
            'grupo': grupo_usuario,
            'data': data,
        })
    else:
        messages.success(request, ('Ocurrió un error, por favor intente nuevamente'))
        return render(request, 'optometria/ver_turno.html',{
            'grupo': grupo_usuario,
            'data': data,
        })
    return render(request, 'optometria/ver_turno.html',{
            'grupo': grupo_usuario,
            'data': data,
        })
#--------------------------------------------------------HC--------------------------------------------
def ver_hc(request):
    grupo_usuario = grupo(request)
    data = Hc.objects.filter(medico_id = request.user.id)
    return render(request, 'optometria/ver_hc.html',{
        'grupo': grupo_usuario,
        'data': data,
        })


def agregar_hc(request):
    grupo_usuario = grupo(request)
    form = HcForm
    if request.method == 'POST':
        form = HcForm(request.POST or None)        
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, ('La Historia Clínica fue agregada exitosamente.'))            
            data = Hc.objects.filter(medico_id = request.user.id)
            return render(request, 'optometria/ver_hc.html',{
                'grupo': grupo_usuario,
                'data': data,
            })
        else:
            messages.success(request, ('Ocurrió un error, por favor intente nuevamente'))
            return render(request, 'optometria/agregar_hc.html',{'formulario':form})
    else:
        return render(request, 'optometria/agregar_hc.html',{'formulario':form})
#-------------------------------------------productos----------------------------------------------