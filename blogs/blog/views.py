from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("Hello, Django!")

def blog(request):
    return HttpResponse("Hello, blog")

def blog_detail(request,id):
    return HttpResponse(f"Hello from {id}")
