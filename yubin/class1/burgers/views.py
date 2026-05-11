from django.shortcuts import render
from burgers.models import Burgers

def burger_list(request):
    burgers = Burgers.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers": burgers,
    }
    return render(request, "burger_list.html", context)