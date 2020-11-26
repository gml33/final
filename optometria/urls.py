from django.urls import path
from . import views


app_name = 'optometria'

urlpatterns = [
    path('', views.index, name='index'),
    #------------------turnos-----------------------------
    path('turno/', views.ver_turnos, name='ver_turnos'),
    path('turno/<int:id>/eliminar', views.eliminar_turno, name='eliminar_turno'),
    path('agregar/turno/', views.agregar_turno, name='agregar_turno'),
    path('editar/turno/<int:id>', views.editar_turno, name='editar_turno'),
    #----------------------HC------------------------------
    path('hc/', views.ver_hc, name='ver_hc'),
    path('agregar/hc/', views.agregar_hc, name='agregar_hc'),
    #----------------------
]