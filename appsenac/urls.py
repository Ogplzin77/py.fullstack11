from django.urls import path
from . import views

app_name = "appsenac"  # Namespace para evitar conflitos

urlpatterns = [
    path("", views.home, name="home"),
    path("cursos/", views.cursos, name="cursos"),
    path("contatos/", views.contatos, name="contatos"),
    path("add-cursos/", views.add_curso, name="add_cursos"),
    path("upload-profile", views.upload_profile, name="upload_profile"),
]
