from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("post title", max_length=100)
    content = models.TextField("post content")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("comment content")

    def __str__(self):
        return f"{self.post.title}'s comment(ID: {self.id})"