from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import Context
from django.template import loader
from AppGrupo5.forms import CargaInstrumento
from AppGrupo5.models import Discos, Instrumento
import datetime
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    return render(request, "AppGrupo5/inicio.html")

def instrumentos(request):
    return render(request, "AppGrupo5/instrumento.html")

def pedal(request):
    return render(request, "AppGrupo5/pedal.html")

def disco(request):
    return render(request, "AppGrupo5/disco.html")

def Carga_Instrumento(request):

    if request.method == 'POST':

        miformulario = CargaInstrumento(request.POST)

        print(miformulario)

        if miformulario.is_valid:
            
            informacion = miformulario.cleaned_data

            instrumento = Instrumento (marca = informacion ['marca'], modelo =informacion ['modelo'], tipoinstrumento=informacion['tipoinstrumento'],color=informacion['color'])

            instrumento.save()

            return render (request,"AppGrupo5/inicio.html")
    else:

        miformulario = CargaInstrumento()

    return render (request,"AppGrupo5/cargainstrumento.html", {"miformulario":miformulario})


def buscarinstrumento(request):

    if  request.GET["tipoinstrumento"]:

	      
        tipoinstrumento = request.GET['tipoinstrumento'] 
        Instrumentos = Instrumento.objects.filter(tipoinstrumento__icontains=tipoinstrumento)

        return render(request, "AppGrupo5/instrumento.html", {"Instrumentos":Instrumentos,"Tipo de Instrumento":tipoinstrumento})
    else: 

	    respuesta = "No se han cargado ningún dato"
        





##  Vistas Basadas en Clases ##

# Instrumentos #

class ListaInstrumentos (ListView):
    model = Instrumento
    template_name = 'AppGrupo5/instrumentoLista.html'
    
class DetalleInstrumento (DetailView):
    model = Instrumento
    template_name = 'AppGrupo5/instrumentoDetalle.html'
    
class CrearInstrumento (CreateView):
    model = Instrumento
    success_url = '/AppGrupo5/listaInstrumentos/'
    fields = ['tipoinstrumento', 'marca', 'modelo', 'color']
    template_name = 'AppGrupo5/instrumentoCrear.html'
    
class ActualizarInstrumento (UpdateView):
    model = Instrumento
    success_url = '/AppGrupo5/listaInstrumentos/'
    fields = ['tipoinstrumento', 'marca', 'modelo', 'color']
    template_name = 'AppGrupo5/instrumentoActualizar.html'
    
class BorrarInstrumento (DeleteView):
    model = Instrumento
    success_url = '/AppGrupo5/listaInstrumentos/'
    template_name = 'AppGrupo5/InstrumentoBorrar_confirm.html'


# Discos #

class ListaDiscos (ListView):
    model = Discos
    template_name = 'AppGrupo5/discosLista.html'
    
class DetalleDiscos (DetailView):
    model = Discos
    template_name = 'AppGrupo5/discosDetalle.html'
    
class CrearDiscos (CreateView):
    model = Discos
    success_url = '/AppGrupo5/listaDiscos/'
    fields = ['album', 'artista', 'fechaLanzamiento']
    template_name = 'AppGrupo5/discoCrear.html'
    
class ActualizarDiscos (UpdateView):
    model = Discos
    success_url = '/AppGrupo5/listaDiscos/'
    fields = ['album', 'artista', 'fechaLanzamiento']
    template_name = 'AppGrupo5/discosActualizar.html'
    
class BorrarDiscos (DeleteView):
    model = Discos
    success_url = '/AppGrupo5/listaDiscos/'
    template_name = 'AppGrupo5/discosBorrar_confirm.html'


# Pedales #
