from django.urls import path
from users.views import login_view, logout_view, signup_view

app_name = "users"

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]