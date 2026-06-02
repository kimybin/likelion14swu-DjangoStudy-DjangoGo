from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )
    like_users = models.ManyToManyField(
        "users.User",
        verbose_name="좋아요한 사용자 목록",
        related_name="like_posts",
        blank=True,
    )
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)
    tags = models.ManyToManyField("posts.HashTag", verbose_name="해시태그 목록", blank=True)


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField("사진", upload_to="post")
    def __str__(self):
        return f"{self.user.username}의 Post(id: {self.id})"

class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)

class HashTag(models.Model):
    name = models.CharField("태그명", max_length=50)

    def __str__(self):
        return self.name

