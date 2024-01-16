from django.shortcuts import render
from AppKF.models import Vinoteca 
from AppKF.forms import Vinosform 
from AppKF.models import Cafeteria
from AppKF.forms import cafeteriaForm 
from AppKF.models import Heladeria
from AppKF.forms import heladeriaForm
from AppKF.forms import CursoForm
from AppKF.models import *
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def inicio (request):
    
    return render(request,"inicio.html")



def agregar_vinos(request):
    if request.method == "POST":
        # VAMOS A GUARDAR LA INFO
        info_formulario = Vinosform (request.POST)

        if info_formulario.is_valid():

            info = info_formulario.cleaned_data
            nueva_vinoteca = Vinoteca(nombre= info["nombre"], empresa = info["empresa"], año = info["año"])

            nueva_vinoteca.save()
            
            return render (request,"todos_los_vinos.html") 

        
    else: 
        nuevo_formulario = Vinosform()

    return render(request, "crear_vinos.html", {"formu": nuevo_formulario}) # Formu es lo que va a leer el html

def ver_vinos(request): 
    vinos = Vinoteca.objects.all()
    return render(request, "todos_los_vinos.html", {"vinos": vinos}) 

####################################################################################################

def cafeteria_1 (request): 
    if request.method == "POST":
        # VAMOS A GUARDAR LA INFO  
        info_formulario = cafeteriaForm(request.POST)


        if info_formulario.is_valid():
            info = info_formulario.cleaned_data

            nueva_cafeteria = Cafeteria(nombre = info["nombre"], apellido = info["apellido"], fecha = info["fecha"])

            nueva_cafeteria.save()
            return render(request, "todas_las_cafeterias.html") 
    else: 
        nuevo_formulario = cafeteriaForm()
    return render(request, "crear_cafeteria.html", {"formu": nuevo_formulario}) # Formu es lo que va a leer el html


def ver_cafeteria(request): 
    cafeterias = Cafeteria.objects.all()
    return render(request, "todos_los_cafes.html", {"cafeterias": cafeterias})

####################################################################################################
def agregar_helados(request):
    if request.method == "POST":
        # VAMOS A GUARDAR LA INFO
        info_formulario = heladeriaForm(request.POST)

        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            nueva_heladeria = Heladeria(nombre=info["nombre"], producto=info["producto"], cantidad=info["cantidad"])
            nueva_heladeria.save()
            
            return render(request, "todos_los_helados.html") 

    else: 
        nuevo_formulario = heladeriaForm()

    return render(request, "crear_helados.html", {"formu": nuevo_formulario}) # Formu es lo que va a leer el html

def ver_helados(request): 
    heladerias = Heladeria.objects.all()
    return render(request, "todos_los_helados.html", {"heladerias": heladerias})


def cursoFormulario(request):
    formulario1 = CursoForm()  # Inicializa el formulario
    if request.method == "POST": 
        formulario1 = CursoForm(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            curso = Curso(nombre = info["Curso"], Camada = info["Camada"])
            curso.save()
            return render(request, "inicio.html")
    
    return render(request, "cursoFormulario.html", {"form1": formulario1})

def busquedaCamada(request):
    return render(request,"inicio.html")

def buscar(request):
    if 'camada' in request.GET and request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__iexact= camada)
        return render(request, "resultados.html", {"cursos": cursos})
    else:
        if 'Curso' in request.GET and request.GET["Curso"]:
            curso = request.GET["Curso"]
            return render(request, "inicio.html", {"Curso": curso, "camada": camada})
        else:
            respuesta = "No enviaste datos"
            return HttpResponse(respuesta)

    