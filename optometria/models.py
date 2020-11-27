from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Turno(models.Model):    
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    paciente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="turno_paciente")
    cumplio = models.BooleanField()
    medico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='turno_medico')

class Hc(models.Model):
    fecha = models.DateField(auto_now_add=False, auto_now= False, blank=True)
    paciente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="hc_paciente")    
    detalle = models.TextField()
    medico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hc_medico')

    def __str__(self):
        return f'{self.paciente}-{self.fecha}'

class Producto(models.Model):
    nombre = models.CharField(max_length=32)
    precio = models.FloatField()
    def __str__(self):
        return f'{self.nombre} ${self.precio}'

class Pedido(models.Model):
    tipo_pago = [
        ("credito","Tarjeta de Crédito"),
        ("debito","Tarjeta de Débito"),
        ("virtual","Billetera Virtual"),
        ("efectivo","Efectivo")

    ]
    estado_pedido = [
        ("pendiente","Pendiente"),
        ("pedido","Pedido"),
        ("taller","Taller"),
        ("finalizado","Finalizado")
    ]
    items = models.ManyToManyField(Producto)
    paciente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Pedido_paciente')
    tipo_de_pago = models.CharField(max_length=10, choices=tipo_pago, default='efectivo')
    estado = models.CharField(max_length=12, choices=estado_pedido, default='pendiente')    

    def precio(self, items):
        precio = 0
        for item in items:
            precio = precio+item.precio
            return precio
    precio = models.FloatField(precio)

    def __str__(self):
        return f"Pedido ID: {self.id}, precio: {self.precio}"
