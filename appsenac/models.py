from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="cursos/", blank=True, null=True)

    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        profile_pic = models.ImageField(
            upload_to="profile_pics/", default="profile_pics/default.jpeg"
        )
        bio = models.TextField(blank=True)

        def __str__(self):
            return self.user.username
