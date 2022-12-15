from django.db import models

# Create your models here.
class Donation(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
