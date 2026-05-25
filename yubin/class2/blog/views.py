from django.shortcuts import render, redirect
from blog.models import Post, Comment

def post_list(request):
    posts = Post.objects.all() # 모든 Post 객체를 가진 QuerySet

    # 템플릿에 전달할 dict
    context = {
        'posts': posts,
    }

    # 3번째 인수로 템플릿에 데이터를 전달
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_content = request.POST['comment']
        Comment.objects.create(
            post=post,
            content=comment_content
        )
    context = {
        "post" : post,
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST":
        print("method POST")
        title = request.POST['title']
        content = request.POST['content']
        thumnail = request.FILES['thumbnail']
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumnail,
        )
        return redirect(f"/posts/{post.id}/")
    else:
        print("method POST")

    return render(request, "post_add.html")