from django.urls import path
from . import views


app_name = 'optometria'


urlpatterns = [
    path('', views.index, name='index'),
    #------------------------turnos--------------------------------------------
    path('turno/', views.ver_turnos, name='ver_turnos'),
    path('agregar/turno/', views.agregar_turno, name='agregar_turno'),
    path('editar/turno/<int:id>', views.editar_turno, name='editar_turno'),
    path('turno/<int:id>/eliminar', views.eliminar_turno, name='eliminar_turno'),    
    #------------------------HC------------------------------------------------
    path('hc/', views.ver_hc, name='ver_hc'),
    path('agregar/hc/', views.agregar_hc, name='agregar_hc'),
    path('editar/hc/<int:id>', views.editar_hc, name='editar_hc'),
    path('hc/<int:id>/eliminar', views.eliminar_hc, name='eliminar_hc'),
    #------------------------Productos-----------------------------------------
    path('producto/', views.ver_producto, name='ver_producto'),
    path('agregar/producto/', views.agregar_producto, name='agregar_producto'),
    path('editar/producto/<int:id>', views.editar_producto, name='editar_producto'),
    path('producto/<int:id>/eliminar', views.eliminar_producto, name='eliminar_producto'),
]