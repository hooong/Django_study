from django.db import models

# Create your models here.
class Blog(models.Model):
    text = models.TextField()