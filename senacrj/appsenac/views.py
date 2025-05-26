from django.shortcuts import render
from django.conf import settings    
from .models import Curso, UserProfile
from .forms import CursosForm, ProfileForm
import os

def home (request):
    return render(request, 'appsenac/home.html') 

def cursos (request):
    cursos =Cursos.objects.filter (disponivel=True)
    return render (request, 'appsenac/cursos.html' {'cursos': cursos})

def contatos(request):
    return render(request, 'appenac/contatos.html')


def list_profile_pics(request):
    
    pics_path = os.path.join(settings.MEDIA_ROOT, 'profile_pics')
    pictures = [f for f in os.listdir(pics_path) if f.endswith(('.jpg', '.png'))]
     return render(request, 'list_pics.html', {'pictures': pictures})
 
 def add_cursos(request):
     if request.method == 'POST':
        form = CursosForm(request.POST, request.FILES)  # Note o request.FILES!
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursosForm()
    return render(request, 'appsenac/add_cursos.html', {'form': form})

def upload_profile(request):
    if request.method == 'POST':
        form = CursosForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = CursosForm()
    return render(request, 'senacapp/upload_profile.html', {'form': form})