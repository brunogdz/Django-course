from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')

def homepage(request):
    return HttpResponse("Home page")

def say_hello(request):
    return HttpResponse("HEY, here I say hello!!")