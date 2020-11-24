def es_medico(user):
    return user.groups.filter(name='medicos').exists()

'''

ver
crear
editar
eliminar

caso secretaria:
    ver turno-
    crear turno-
    editar turno-
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
'''