from django import forms

class form_empleados(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    area = forms.CharField(max_length=30)
    empresa = forms.CharField(max_length=30)