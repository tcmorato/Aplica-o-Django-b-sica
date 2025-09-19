from django.db import models
# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/')
    descricao = models.TextField()