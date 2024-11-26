from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def firstapp(request):
    return HttpResponse('My first Django app')