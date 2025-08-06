from django.db import models

# Create your models here.
class Magneto_User(models.Model):
    name = models.CharField(max_length=100)
