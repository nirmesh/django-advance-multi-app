from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def my_app(request):
    d=datetime.datetime.now()
    s="<h1>my current  time "+str(d)+"</h1>"
    return HttpResponse(s)

def first(request):
    return HttpResponse("<h1>first</h1>")

def second(request):
    return HttpResponse("<h1>second</h1>")

def third(request):
    return HttpResponse("<h1>third<h1>")

