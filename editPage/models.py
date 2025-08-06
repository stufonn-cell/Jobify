from django.db import models

# Create your models here.
class Avatar(models.Model):
    avatar_image = models.ImageField(null=False, upload_to="avatars/")
    
