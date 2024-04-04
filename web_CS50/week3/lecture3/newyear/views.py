from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("New Year index page")