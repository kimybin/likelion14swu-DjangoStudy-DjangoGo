from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup_view(request):
    """회원가입 뷰"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 성공 시 자동으로 로그인 처리
            return redirect("posts:feeds")  # 가입 후 피드 페이지로 이동
    else:
        form = UserCreationForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    """로그인 뷰"""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("posts:feeds")  # 로그인 후 피드 페이지로 이동
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    """로그아웃 뷰"""
    if request.method == "POST":
        logout(request)
        return redirect("users:login")
    return redirect("posts:feeds")