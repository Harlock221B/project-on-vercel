from django.shortcuts import render, Http404, get_object_or_404
from .models import Perfil

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre_nos.html')

def oquefazemos(request):
    return render(request,'oque_fazemos.html')


# Create your views here.
