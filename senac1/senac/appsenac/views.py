from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    cursos = [
        {"nome": "Python para Iniciantes", "descricao": "Aprenda Python do zero!"},
        {"nome": "Desenvolvimento Web com Django", "descricao": "Crie sites dinâmicos com Django."},
        {"nome": "HTML & CSS Essencial", "descricao": "Domine a base da web."}
    ]
    return render(request, 'appsenac/index.html', {'cursos': cursos})

def lista_cursos(request):
    cursos = [
        {"nome": "Python para Iniciantes", "descricao": "Aprenda Python do zero!"},
        {"nome": "Django Avançado", "descricao": "Crie aplicações web completas."},
        {"nome": "Front-End com React", "descricao": "Interfaces modernas com React."}
    ]
    return render(request, 'appsenac/cursos.html', {'cursos': cursos})

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('cadastro')
    return render(request, 'appsenac/cadastro.html')

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contato')
    return render(request, 'appsenac/contato.html')
