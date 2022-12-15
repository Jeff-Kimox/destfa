from django.db import models

# Create your models here.
class JoinUs(models.Model):
    title = models.CharField(max_length=100)
    email  = models.EmailField()

    def __str__(self):
        return self.email
