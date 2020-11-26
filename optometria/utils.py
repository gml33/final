'''
ver
crear
editar
eliminar

caso secretario:
    ver turno-
    crear turno-
    editar turno
    eliminar turno-

caso medico:
    agregar hc-
    ver pacientes propios-

caso ventas:
    crear pedido-
    modificar pedido-

caso taller:
    ver pedido-
    modificar pedido-

caso gerencia:
    ver turno-
    ver hc-
    ver pacientes-
    ver medicos-
    ver productos-
    ver pedidos-
    ver reportes-

class venta(models.Model):
    id_paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fecha_venta = models.DateField(default=datetime.datetime(2000,1,31))
    monto_total = models.CharField(max_length=64)
    id_User = models.ForeignKey(User, on_delete = models.CASCADE)
   




        <input type="text", name="paciente", 
    {{ formulario.as_p }}

     '''