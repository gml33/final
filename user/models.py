from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.

class User(AbstractUser):
    roles = [
        ('secretario','Secretario'),
        ('medicos','Medico'),
        ('venta','Ventas'),
        ('taller','Taller'),
        ('gerencia','Gerente'),
        ('paciente','Paciente')]
    rol = models.CharField(max_length=16, choices=roles, default='paciente')