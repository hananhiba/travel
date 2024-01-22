
from django.shortcuts import render
from . models import Place

# Create your views here.


def fun(request):
    obj = Place.objects.all()
    return render(request,"index.html",{'object':obj})

