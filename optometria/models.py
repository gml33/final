from django.db import models
from django.contrib.auth.models import User, Group

class Medico(models.Model):
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    especialidad = models.CharField(max_length=64)
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.especialidad}'

class Paciente(models.Model):
    nombre = models.CharField(max_length=32)
    apellido = models.CharField(max_length=32)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Hc(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="Hc_paciente")
    fecha = models.DateTimeField(auto_now=True)
    detalle = models.TextField()
    medico = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Hc_medico')

    def __str__(self):
        return f'{self.Paciente}-{self.fecha}'

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
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='Pedido_paciente')
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


class Turno(models.Model):
    fecha = models.DateTimeField(auto_now=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="turno_paciente")
    cumplio = models.BooleanField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='turno_medico')
