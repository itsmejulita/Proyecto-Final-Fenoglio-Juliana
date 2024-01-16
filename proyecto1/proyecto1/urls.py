"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from AppKF.views import *

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ("nueva_vinoteca", agregar_vinos),
    path ("Vinoteca", ver_vinos, name = "Vinos"),
    path ("formu", agregar_vinos),
    path ("inicio", inicio, name = "Inicio"),
    path ("nueva_cafeteria", cafeteria_1),
    path ("cafeteria_1", ver_cafeteria, name = "Café"),
    path ("formu", cafeteria_1),
    path ("nueva_heladeria", agregar_helados),
    path ("Heladeria", ver_helados, name = "Helados"), 
    path('cursoFormulario/', cursoFormulario, name='FormularioCurso'),
    path ("buscarCamada/", busquedaCamada, name = "BuscarCamada"),
    path ("buscar/", buscar, name = "ResultadoCamada") 
]
