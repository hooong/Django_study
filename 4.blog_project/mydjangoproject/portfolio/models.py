from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/')  #media폴더안에 존재하는 images폴더를 가리킴.
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title