from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def welcome_demo(request):
    return HttpResponse("Welcome,demo!")