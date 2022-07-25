from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    wingspan = models.IntegerField()
