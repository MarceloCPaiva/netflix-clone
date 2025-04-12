from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("ACAO", "Ação"),
    ("ANIMACAO", "Animação"),
    ("AVENTURA", "Aventura"),
    ("COMEDIA", "Comédia"),
    ("DOCUMENTARIO", "Documentário"),
    ("DRAMA", "Drama"),
    ("FICCAO", "Ficção Científica"),
    ("MUSICAL", "Musical"),
    ("ROMANCE", "Romance"),
    ("SUSPENSE", "Suspense"),
    ("TERROR", "Terror")
)

#Criar Filme

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=2000)
    categoria = models.CharField(max_length=25, choices=LISTA_CATEGORIAS)
    visualisacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo