from django.db import models

# DB -> 변경사항이 있으면 python manage.py makemigrations
class Post(models.Model):
    title = models.CharField("포스트 제목", max_length=100)
    content = models.TextField("포스트 내용")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="posts/", blank=True)

    def __str__(self): # __는 밑줄(_, underscore)을 두 번 쓴 것
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID:  {self.id})"

