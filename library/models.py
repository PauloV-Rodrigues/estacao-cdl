from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from PIL import Image

class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    theme = models.CharField(null=True, max_length=255)
    author = models.CharField(max_length=255)
    body = models.TextField()
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("library:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']

class Student(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    photo = models.ImageField(default='default.jpg')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    assunto = models.CharField(max_length=255)
    email = models.EmailField()
    nome = models.CharField(max_length=255)
    mensagem = models.TextField()

    def __str__(self):
        return self.email