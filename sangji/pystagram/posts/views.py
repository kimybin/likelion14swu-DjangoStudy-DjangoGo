from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.forms import PostForm

@login_required
def feeds(request):
    # 💡 모든 Post를 최신글 순(created_at)으로 정렬해서 가져옵니다.
    posts = Post.objects.all().order_by("-created_at")

    context = {
        "posts": posts,
    }
    return render(request, "posts/feeds.html", context)


@login_required
def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/posts/feeds/")
    else:
        form = Form = PostForm()

    context = {"form": form}
    return render(request, "posts/post_add.html", context)