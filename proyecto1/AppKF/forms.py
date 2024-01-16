from django import forms 

class Vinosform(forms.Form):

    nombre = forms.CharField(max_length=30)
    empresa = forms.CharField(max_length=30)
    año = forms.IntegerField()


class cafeteriaForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fecha = forms.IntegerField()



class heladeriaForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    producto = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()

class CursoForm(forms.Form):
    Curso = forms.CharField(max_length=30)
    Camada = forms.IntegerField()