from django import forms
from .models import Curso, UserProfile


class CursosForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nome", "descricao", "disponivel", "professor", "imagem", "preco"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_pic"]
