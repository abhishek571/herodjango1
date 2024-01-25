from django.shortcuts import render
from django.http import HttpResponse
from.models import DC
# Create your views here.

def superman(request):
    con=DC.objects.all()
    return render(request,'dc/superman.html',{'con':con})

def hulk(request):
    return render(request,'dc/hulk.html')
