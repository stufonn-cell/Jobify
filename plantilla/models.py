from django.db import models
from User.models import Magneto_User


# Create your models here.
class TemplateModel(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50, null=False, default='N/A')
    desc = models.CharField(max_length=500, null=False, default='N/A')
    city = models.CharField(max_length=100, null=False, default='N/A')
    color = models.CharField(max_length=30, null=False, default='#fff')
    font = models.CharField(max_length=30, null=False, default='sans-serif')
    font_color = models.CharField(max_length=30, null=False, default='#333')
    brand_logo = models.ImageField(null=True, upload_to="brand_logos/")
