from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    blog_hit = models.PositiveIntegerField(default = 0)
    # like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = 'like_user_set', through='Like') 

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    class Meta:
        ordering = ['pub_date']

    #조회수 증가
    def update_counter(self):
        self.blog_hit = self.blog_hit + 1
        self.save()

    # #좋아요
    # def like_count(self):
    #     return self.like_user_set.count()

#댓글 모델
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.comment_contents

# class Like(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='likes')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
