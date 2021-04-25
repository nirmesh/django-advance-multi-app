from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def my_app(request):
    d=datetime.datetime.now()
    s="<h1>my current  time "+str(d)+"</h1>"
    return HttpResponse(s)