from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def spiderman(request):
    con={'villan':'zod'}
    return render(request,'dc/spiderman.html',con)

def ironman(request):
    con={'villan':'zod'}
    return render(request,'dc/ironman.html',con)

