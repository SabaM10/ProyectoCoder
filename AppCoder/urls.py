from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('create_empleados/', create_empleados),
    path('update_empleados/<empleado_id>', update_empleados),        
    path('read_empleados/', read_empleados),
    path('delete_empleados/<empleado_id>', delete_empleados),
    path('create_administrativos/', create_administrativos),
    path('read_administrativos/', read_administrativos),
    path('update_administrativos/<administrativo_id>', update_administrativos),
    path('delete_administrativos/<administrativo_id>', delete_administrativos),
    path('buscar_empleado/', buscar_empleado,)
]