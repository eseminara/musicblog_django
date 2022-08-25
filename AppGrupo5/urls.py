from unicodedata import name
from django.urls import path

from AppGrupo5 import views

urlpatterns = [
    
    path('instrumentos',views.instrumentos, name="instrumentos"),
    path('pedal', views.pedal, name= "pedal"),
    path('disco',views.disco, name= "disco"),
    path('', views.inicio, name="inicio"),
    path('cargainstrumento/',views.Carga_Instrumento,name="cargainstrumento"),
    path('buscarinstrumento/',views.buscarinstrumento),

#CRUD VISTA BASADA EN CLASE#

#Instrumentos#
    
    path('listaInstrumentos/',views.ListaInstrumentos.as_view(), name='Lista'),
    path('detalleInstrumentos/<pk>',views.DetalleInstrumento.as_view(), name='Detalle'),
    path('crearInstrumentos/',views.CrearInstrumento.as_view(), name='Crear'),
    path('actualizarInstrumentos/<pk>',views.ActualizarInstrumento.as_view(), name='Actualizar'),
    path('borrarInstrumentos/<pk>',views.BorrarInstrumento.as_view(), name='Borrar'),
    
#Discos#
    
    path('listaDiscos/',views.ListaDiscos.as_view(), name='ListaDiscos'),
    path('detalleDiscos/<pk>',views.DetalleDiscos.as_view(), name='DetalleDiscos'),
    path('crearDiscos/',views.CrearDiscos.as_view(), name='CrearDiscos'),
    path('actualizarDiscos/<pk>',views.ActualizarDiscos.as_view(), name='ActualizarDiscos'),
    path('borrarDiscos/<pk>',views.BorrarDiscos.as_view(), name='BorrarDiscos'),







]