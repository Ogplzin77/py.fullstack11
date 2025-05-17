from django.shortcuts import render
from .models import Produtos
# Create your views here.

def home(request):
  return render(request, 'appAntAcademia/home.html')

def produtos(request):
  produtos= Produtos.objects.all()
  return render(request, 'appAntAcademia/produtos.html', {'produtos':produtos})

def contatos(request):
  return render(request, 'appAntAcademia/contatos.html')