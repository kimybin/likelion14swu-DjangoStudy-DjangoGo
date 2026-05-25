from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자"
    )
    post_image = models.ImageField("포스트 이미지", upload_to="posts/photo")
    content = models.TextField("본문")
    created_at = models.DateTimeField("생성일시", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}의 포스트(id: {self.id})"