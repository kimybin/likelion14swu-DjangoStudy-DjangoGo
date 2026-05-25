from django.urls import path
from posts.views import feeds, post_add

urlpatterns = [
    path("feeds/", feeds),
    path("post_add/", post_add),
]