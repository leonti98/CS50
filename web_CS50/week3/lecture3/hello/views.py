from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def levan(request):
    return HttpResponse("Hello, Levan")

def david(request):
    return HttpResponse("Hello, David")

def greet(request, name):
    return HttpResponse(f"Hello, {name}")