from django.db import models
from imagekit.models import ImageSpecField      # 이 함수로서 썸네일을 만들어냄
from imagekit.processors import ResizeToFill    # 크기조정을 쉽게 해주는 기능

# Create your models here.
class Blog(models.Model):
    text = models.TextField()

class Pictures(models.Model):
    text  = models.TextField()
    image = models.ImageField(upload_to = "pic")
    image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(120,300)])      # 이미지파일을 지정(source)해서 썸네일을 만들어준다. processors는 사이즈를 지정.
