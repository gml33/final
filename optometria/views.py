from django.shortcuts import render, redirect
from .utils import *
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model




User = get_user_model()



def index(request):
    return render(request, 'optometria/index.html',{
        'grupo': request.user.rol
    })
#----------------------------------------------turnos----------------------------------------------
def ver_turnos(request):
    data = Turno.objects.all()
    return render(request, 'optometria/ver_turno.html',{
        'grupo': request.user.rol,
        'data': data,
        })

def agregar_turno(request):
    form = TurnoForm
    if request.method == 'POST':
        form = TurnoForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.cumplio = False
            form.save()
            messages.success(request, ('El turno fue agregado exitosamente.'))
            data = Turno.objects.all()
            return render(request, 'optometria/ver_turno.html',{
                'grupo': request.user.rol,
                'data': data,
            })
        else:
            messages.success(request, ('Ocurrió un error, por favor intente nuevamente'))
            return render(request, 'optometria/agregar_turno.html',{'formulario':form})
    else:
        return render(request, 'optometria/agregar_turno.html',{'formulario':form})


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
    data = Hc.objects.filter(medico_id = request.user.id)
    return render(request, 'optometria/ver_hc.html',{
        'grupo': request.user.rol,
        'data': data,
        })


def agregar_hc(request):
    form = HcForm
    if request.method == 'POST':
        form = HcForm(request.POST or None)        
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, ('La Historia Clínica fue agregada exitosamente.'))            
            data = Hc.objects.filter(medico_id = request.user.id)
            return render(request, 'optometria/ver_hc.html',{
                'grupo': request.user.rol,
                'data': data,
            })
        else:
            messages.success(request, ('Ocurrió un error, por favor intente nuevamente'))
            return render(request, 'optometria/agregar_hc.html',{'formulario':form})
    else:
        return render(request, 'optometria/agregar_hc.html',{'formulario':form})
#-------------------------------------------productos----------------------------------------------