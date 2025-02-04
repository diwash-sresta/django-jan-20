from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def demo_blog(request):
        post = Post.objects.all()
    
        return render(request,"demo2.html",{'post':post})