from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def superman(request):
    con={'villan':'zod'}
    return render(request,'dc/superman.html',con)

def hulk(request):
    return render(request,'dc/hulk.html')
