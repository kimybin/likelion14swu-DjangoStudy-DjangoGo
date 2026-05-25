from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 사용자에게 입력받을 필드만 지정 (작성자와 생성일시는 백엔드에서 자동 처리)
        fields = [
            "post_image",
            "content",
        ]