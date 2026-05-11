from django.urls import path
from . import views

urlpatterns = [
    path("", views.burger_list, name="burger_list"),
]