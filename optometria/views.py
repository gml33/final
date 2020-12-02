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
from django.core.exceptions import ObjectDoesNotExist


User = get_user_model()


def index(request):
    return render(request, 'optometria/index.html',{
        'grupo': request.user.rol
    })
#----------------------------------------------turnos----------------------------------------------
def ver_turnos(request):
    if len(Turno.objects.all()) > 0:
        data = Turno.objects.all().order_by('-fecha')
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
        data = Hc.objects.filter(medico_id = request.user.id).order_by('-fecha')
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

def ver_producto(request):
    if len(Producto.objects.all()) > 0:
        data = Producto.objects.all()
    else:
        data = None
    return render(request, 'optometria/ver_producto.html',{
        'grupo': request.user.rol,
        'data': data,
        })

def agregar_producto(request):    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            precio = int(form.cleaned_data['precio'])
            form.save()
            messages.success(request, ('Producto Registrado.'))
            return HttpResponseRedirect(reverse('optometria:ver_producto'))
        else:
            form = HcForm()
    return render(request, 'optometria/agregar_producto.html',{
        'grupo': request.user.rol,
        'pacientes':User.objects.filter(rol='paciente'),
        'medico':request.user.id
        })


def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.user.rol == 'venta':
        if request.method == 'GET':
            form = ProductoForm(instance=producto)
        else:
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                precio = int(form.cleaned_data['precio'])
                form.save()
                messages.success(request, ('Se editó el producto.'))
                return HttpResponseRedirect(reverse('optometria:ver_producto'))
    else:
        form = ProductoForm()
    return render(request, 'optometria/editar_producto.html',{
        'grupo': request.user.rol,
        'producto': Producto.objects.get(id=id)
        })

def eliminar_producto(request, id):
    data = Producto.objects.all()
    producto = Producto.objects.get(id=id)
    if request.user.rol == 'venta':
        producto.delete()
        messages.success(request, ('Se eliminó el producto.'))
        return render(request, 'optometria/ver_producto.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    else:
        messages.success(request, ('Ocurrió un error, estamos en la sopa..... :('))
        return render(request, 'optometria/ver_producto.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    return render(request, 'optometria/ver_producto.html',{
            'grupo': request.user.rol,
            'data': data,
        })
#----------------------------Pedidos-----------------------------------------------------

def ver_pedido(request):
    if len(Pedido.objects.all()) > 0:
        data = Pedido.objects.all()
    else:
        data = None
    return render(request, 'optometria/ver_pedido.html',{
        'grupo': request.user.rol,
        'data': data,
        })


def agregar_pedido(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()        
        precio = 0
        for item in list(request.POST.getlist('items')):
            producto = Producto.objects.get(id=item)
            precio = precio + producto.precio
        if request.POST['pide_lente'] == 'True':
            precio = precio + int(request.POST['precio'])
        else:
            pass
        request.POST['vendedor'] = request.user.id
        request.POST['precio'] = precio
        form_pedido = PedidoForm(request.POST)
        form_lente = LenteForm(request.POST)        
        if form_pedido.is_valid():
            form_pedido.save()            
            if request.POST['pide_lente'] == 'True':                
                request.POST['distancia'] = request.POST['distancia']
                request.POST['lado'] = request.POST['lado']
                request.POST['armazon'] = request.POST['armazon']
                request.POST['precio'] = request.POST['precio']
                request.POST['pedido'] = Pedido.objects.latest('pk').pk
                form_lente = LenteForm(request.POST)
                if form_lente.is_valid():
                    form_lente.save()
                    messages.success(request, ('Pedido con lentes registrados.'))
                    return HttpResponseRedirect(reverse('optometria:ver_pedido'))
                else:
                    print(form_lente.errors)
                    messages.success(request, ('Pedido no registrado. lente_form mal hecho'))
                    form_pedido = PedidoForm(request.POST)
                    form_lente = LenteForm(request.POST)
            else:                
                messages.success(request, ('Pedido Registrado.'))
                return HttpResponseRedirect(reverse('optometria:ver_pedido'))
        else:
            print(form_pedido.errors)
            messages.success(request, ('Pedido no registrado. pedido_form mal hecho'))
            form_pedido = PedidoForm(request.POST)
            form_lente = LenteForm(request.POST)
    return render(request, 'optometria/agregar_pedido.html',{
        'grupo': request.user.rol,
        'pacientes':User.objects.filter(rol='paciente'),
        'medico':request.user.id,
        'productos': Producto.objects.all(),
        })


def editar_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    if request.user.rol == 'venta':
        if request.method == 'GET':
            form = PedidoForm(instance=pedido)
        else:
            form = PedidoForm(request.POST, instance=pedido)
            if form.is_valid():
                form.save()
                messages.success(request, ('Se editó el pedido.'))
                return HttpResponseRedirect(reverse('optometria:ver_pedido'))
    else:
        form = PedidoForm()
    return render(request, 'optometria/editar_pedido.html',{
        'grupo': request.user.rol,
        'pedido': Pedido.objects.get(id=id)
        })

def eliminar_pedido(request, id):
    data = Pedido.objects.all()
    pedido = Pedido.objects.get(id=id)
    #lente = Lente.objects.get(pedido=id)
    if request.user.rol == 'venta':
        pedido.delete()
        #lente.delete()
        messages.success(request, ('Se eliminó el pedido.'))
        return render(request, 'optometria/ver_pedido.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    else:
        messages.success(request, ('Ocurrió un error, estamos en la sopa..... :('))
        return render(request, 'optometria/ver_pedido.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    return render(request, 'optometria/ver_pedido.html',{
            'grupo': request.user.rol,
            'data': data,
        })

def detalle_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    paciente = User.objects.get(id=pedido.paciente.id)
    items = Producto.objects.filter(pedido=id)
    vendedor = User.objects.get(id=pedido.vendedor.id)

    try:
        lente = Lente.objects.get(pedido=id)
    except ObjectDoesNotExist:
        lente = None
    
    return render(request, 'optometria/detalle_pedido.html',{
        'grupo': request.user.rol,
        'pedido': Pedido.objects.get(id=id),
        'lente': lente,
        'paciente':paciente,
        'items':items,
        'vendedor':vendedor,
        })