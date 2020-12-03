from django.shortcuts import render, redirect, reverse
from .utils import *
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist


User = get_user_model()


def index(request):
    ultima_semana = datetime.now() - timedelta(days=7)
    ultimo_mes = datetime.now() - timedelta(days=30)

    cumplio_semana = Turno.objects.filter(fecha__gte=ultima_semana).filter(cumplio=True)
    cumplio_mes = Turno.objects.filter(fecha__gte=ultimo_mes).filter(cumplio=True)

    no_cumplio_semana = Turno.objects.filter(fecha__gte=ultima_semana).exclude(cumplio=True)
    no_cumplio_mes = Turno.objects.filter(fecha__gte=ultimo_mes).exclude(cumplio=True)

    pedidos_semana = Pedido.objects.filter(fecha__gte=ultima_semana)
    pedidos_mes = Pedido.objects.filter(fecha__gte=ultimo_mes)
    if len(Turno.objects.all()) > 0:
        turnos = Turno.objects.all().order_by('-fecha')
    else:
        turnos = None
    if len(Hc.objects.filter(medico_id=request.user.id)) > 0:
        hcs = Hc.objects.filter(medico_id = request.user.id).order_by('-fecha')
    else:
        hcs = None
    if len(Pedido.objects.all()) > 0:
        pedidos = Pedido.objects.all()
    else:
        pedidos = None
    return render(request, 'optometria/index.html',{
        'grupo': request.user.rol,
        'turnos': turnos,
        'hcs':hcs,
        'pedidos':pedidos,
        'cumplio_semana': cumplio_semana,
        'cumlpio_mes':cumplio_mes,
        'no_cumplio_semana':no_cumplio_semana,
        'no_cumplio_mes':no_cumplio_mes,
        'pedidos_semana': pedidos_semana,
        'pedidos_mes': pedidos_mes,
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
            return HttpResponseRedirect(reverse('optometria:index'))
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
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    else:
        messages.success(request, ('Ocurrió un error, por favor intente nuevamente'))
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'data': data,
        })
    return render(request, 'optometria/index.html',{
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
            return HttpResponseRedirect(reverse('optometria:index'))
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
                return HttpResponseRedirect(reverse('optometria:index'))
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
        print(request.POST)
        precio_pedido = 0
        precio_lente = 0
        for item in list(request.POST.getlist('items')):
            producto = Producto.objects.get(id=item)
            precio_pedido = precio_pedido + producto.precio
        if request.POST['pide_lente'] == 'True':
            precio_lente = int(request.POST['precio'])
            precio_total = precio_pedido + precio_lente
        else:
            pass
        request.POST['vendedor'] = request.user.id
        request.POST['precio'] = precio_pedido
        form_pedido = PedidoForm(request.POST)
        form_lente = LenteForm(request.POST)        
        if form_pedido.is_valid():
            form_pedido.save()            
            if request.POST['pide_lente'] == 'True':                
                request.POST['distancia'] = request.POST['distancia']
                request.POST['lado'] = request.POST['lado']
                request.POST['armazon'] = request.POST['armazon']
                request.POST['precio'] = precio_lente #precio del lente
                request.POST['pedido'] = Pedido.objects.latest('pk').pk
                form_lente = LenteForm(request.POST)
                if form_lente.is_valid():
                    form_lente.save()
                    messages.success(request, ('Pedido con lentes registrados.'))
                    return HttpResponseRedirect(reverse('optometria:index'))
                else:
                    print(form_lente.errors)
                    messages.success(request, ('Pedido no registrado. lente_form mal hecho'))
                    form_pedido = PedidoForm(request.POST)
                    form_lente = LenteForm(request.POST)
            else:                
                messages.success(request, ('Pedido Registrado.'))
                return HttpResponseRedirect(reverse('optometria:index'))
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
    pedidos = Pedido.objects.all()
    pedido_a_eliminar = Pedido.objects.get(id=id)
    #lente = Lente.objects.get(pedido=id)
    if request.user.rol == 'venta':
        pedido_a_eliminar.delete()
        #lente.delete()
        messages.success(request, ('Se eliminó el pedido.'))
        if len(Pedido.objects.all()) > 0:
            pedidos = Pedido.objects.all()
        else:
            pedidos = None 
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })
    else:
        messages.success(request, ('Ocurrió un error, estamos en la sopa..... :('))
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })
    return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
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
    
    if lente != None:
        precio_final = pedido.precio + lente.precio
    else:
        precio_final = pedido.precio
        
    return render(request, 'optometria/detalle_pedido.html',{
        'grupo': request.user.rol,
        'pedido': Pedido.objects.get(id=id),
        'lente': lente,
        'paciente':paciente,
        'items':items,
        'vendedor':vendedor,
        'precio_final': precio_final,
        })


def finalizar_pedido(request, id):
    pedidos = Pedido.objects.all()
    if request.user.rol == 'taller':
        Pedido.objects.filter(id=id).update(estado='finalizado')
        messages.success(request, ('Se finalizó el pedido.'))
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })
    else:
        messages.success(request, ('Ocurrió un error, estamos en la sopa..... :('))
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })
    return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })

def estado_pedido(request, id):
    pedidos = Pedido.objects.all()
    if request.user.rol == 'venta':
        Pedido.objects.filter(id=id).update(estado='pedido')
        messages.success(request, ('Se actualizó el estado del pedido.'))
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })
    else:
        messages.success(request, ('Ocurrió un error, estamos en la sopa..... :('))
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })
    return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })

def estado_taller(request, id):
    pedidos = Pedido.objects.all()
    if request.user.rol == 'venta':
        Pedido.objects.filter(id=id).update(estado='taller')
        messages.success(request, ('Se actualizó el estado del pedido.'))
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })
    else:
        messages.success(request, ('Ocurrió un error, estamos en la sopa..... :('))
        return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })
    return render(request, 'optometria/index.html',{
            'grupo': request.user.rol,
            'pedidos': pedidos,
        })

#----------------------------Reportes para la gerencia-----------------------------------
def ver_reportes(request):
    ultima_semana = datetime.now() - timedelta(days=7)
    ultimo_mes = datetime.now() - timedelta(days=30)

    cumplio_semana = Turno.objects.filter(fecha__gte=ultima_semana).filter(cumplio=True)
    cumplio_mes = Turno.objects.filter(fecha__gte=ultimo_mes).filter(cumplio=True)

    no_cumplio_semana = Turno.objects.filter(fecha__gte=ultima_semana).exclude(cumplio=True)
    no_cumplio_mes = Turno.objects.filter(fecha__gte=ultimo_mes).exclude(cumplio=True)

    pedidos_semana = Pedido.objects.filter(fecha__gte=ultima_semana)
    pedidos_mes = Pedido.objects.filter(fecha__gte=ultimo_mes)

    print(cumplio_semana)
    return render(request, "optometria/index.html",{
            'grupo': request.user.rol,
            'cumplio_semana': cumplio_semana,
            'cumlpio_mes':cumplio_mes,
            'no_cumplio_semana':no_cumplio_semana,
            'no_cumplio_mes':no_cumplio_mes,
            'pedidos_semana': pedidos_semana,
            'pedidos_mes': pedidos_mes,
            })