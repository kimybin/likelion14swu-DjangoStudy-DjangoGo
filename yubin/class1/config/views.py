import keyword

from django.shortcuts import render
from django.template.context_processors import request

from burgers.models import Burgers

def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burgers.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers": burgers,
    }

    return render(request, "burger_list.html", context)

def burger_search(request):
    keyword = request.GET.get("keyword")

    if keyword is not None:
        burgers = Burgers.objects.filter(name__contains=keyword)

    else:
        burgers = Burgers.objects.none()

    context = {
        "burgers": burgers,
    }

    return render(request, "burger_search.html", context)
