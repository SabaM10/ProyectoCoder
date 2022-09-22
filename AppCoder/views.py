from tkinter import E
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.forms import form_empleados
from AppCoder.models import *
# Create your views here.
def index(request):

      return render(request, 'padre.html')

def create_empleados(request):
      if request.method == 'POST':
            empleado = Empleado(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], area=request.POST['area'], empresa=request.POST['empresa'])
            empleado.save()
            empleados = Empleado.objects.all()
            return render(request, 'empleadosCRUD/read_empleados.html', {'empleados': empleados})
      return render(request, 'empleadosCRUD/create_empleados.html')

def read_empleados(request = None):
      empleados = Empleado.objects.all()
      return render(request, 'empleadosCRUD/read_empleados.html', {'empleados': empleados})

def update_empleados(request, empleado_id):
      empleado = Empleado.objects.get(id=empleado_id)

      if request.method == 'POST':
            formulario = form_empleados(request.POST)

            if formulario.is_valid():
                  empleado.nombre = request.POST['nombre']
                  empleado.apellido = request.POST['apellido']
                  empleado.email = request.POST['email']
                  empleado.area = request.POST['area']
                  empleado.empresa = request.POST['empresa']
                  empleado.save()
                  read_empleados()
                  empleados = Empleado.objects.all()
                  return render(request, 'empleadosCRUD/read_empleados.html', {'empleados': empleados})
      else:
            formulario = form_empleados(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'email': empleado.email, 'area': empleado.area, 'empresa': empleado.empresa})
      return render(request, 'empleadosCRUD/update_empleados.html', {'empleado': empleado})

def delete_empleados(request, empleado_id):
      empleado = Empleado.objects.get(id=empleado_id)
      empleado.delete()

      empleados = Empleado.objects.all()
      return render(request, 'empleadosCRUD/read_empleados.html', {'empleados': empleados})
