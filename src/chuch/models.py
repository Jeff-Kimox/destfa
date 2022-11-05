from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from tinymce import models as tinymce_models

class User(AbstractUser):
    pass


class Sermon(models.Model):
    CATEGORIES = (
        ('SERMON', 'SERMON'),
        ('BIBLESTUDY', 'BIBLESTUDY'),
        ('MIDWEEKSTUDY', 'MIDWEEKSTUDY'),
        ('MORNINGDEVOTION', 'MORNINGDEVOTION'),
    )
    title = models.CharField(max_length=100)
    content = tinymce_models.HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    sermon_from = models.CharField(max_length=100)
    categories = models.CharField(max_length=100, choices=CATEGORIES)
    thumbnail = models.ImageField()
    featured = models.BooleanField()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('sermon-detail', kwargs={
            'id': self.id
        })

    def get_update_url(self):
        return reverse('sermon-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('sermon-delete', kwargs={
            'id': self.id
        })


class Event(models.Model):
    CATEGORIES = (
        ('YOUTH', 'YOUTH'),
        ('MEN', 'MEN'),
        ('WOMEN', 'WOMEN'),
        ('CHILDREN', 'CHILDREN'),
        ('CHURCH', 'CHURCH'),
    )
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    overview = models.TextField()
    thumbnail = models.ImageField()
    time = models.TimeField()
    categories = models.CharField(max_length=100, choices=CATEGORIES)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={
            'id': self.id
        })

    def get_update_url(self):
        return reverse('event-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('event-delete', kwargs={
            'id': self.id
        })

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sermon = models.ForeignKey(Sermon, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.content[0:50]