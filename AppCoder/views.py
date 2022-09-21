from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import *
# Create your views here.
def index(request):

      return render(request, 'padre.html')