from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, "users/login.html")
def logout_view(request):
    return render(request, "users/logout.html")