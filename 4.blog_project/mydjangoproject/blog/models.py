from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    blog_hit = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def update_counter(self):
        self.blog_hit = self.blog_hit + 1
        self.save()

#댓글 모델
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.comment_contents