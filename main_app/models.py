from django.db import models

# Create your models here.
class Finch(models.Model):
    finch_name = models.CharField(max_length=15)
    pub_date = models.DateTimeField('date published')
