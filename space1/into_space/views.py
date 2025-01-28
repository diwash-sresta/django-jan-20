from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def welcome_space(request):
    return HttpResponse("Welcome to the Space1.")