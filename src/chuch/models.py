from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from tinymce import models as tinymce_models

class User(AbstractUser):
    pass


class Sermon(models.Model):
    title = models.CharField(max_length=100)
    content = tinymce_models.HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    sermon_from = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    featured = models.BooleanField()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('sermon-detail', kwargs={
            'id': self.id
        })


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    overview = models.TextField()
    thumbnail = models.ImageField()
    time = models.TimeField()
    categories = models.ManyToManyField("Category")
    featured = models.BooleanField()

    def __str__(self):
        return self.overview

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={
            'id': self.id
        })