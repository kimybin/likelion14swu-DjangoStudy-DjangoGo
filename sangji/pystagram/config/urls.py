from django.contrib import admin
from django.urls import path, include
# 💡 미디어 파일을 서빙하기 위해 필요한 장고 내장 모듈들을 가져옵니다.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
    path("posts/", include("posts.urls")),
]

# 💡 [핵심 추가] 디버그 모드일 때 사용자가 업로드한 미디어 파일 주소를 연결해 줍니다.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)