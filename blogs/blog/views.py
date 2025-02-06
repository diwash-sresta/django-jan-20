from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog

def helloworld(request):
    data = {
        "title": "Welcome to Django Templates",
        "items": ["Python","Django","Templates"]
    }
    return render(request,"home.html",data)


def blog(request):
    return HttpResponse("Hello, blog")

# def blog_detail(request,id):
#     return HttpResponse(f"Hello from {id}")

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request,'blog_list.html',{'blogs':blogs})

# View a single blog post
def blog_detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog_detail.html',{'blog':blog})

# Create a new blog post
def blog_create(request):
    if request.method =="POST":
        title = request.POST['title']
        content = request.POST['content']
        Blog.objects.create(title=title, content=content)
        return redirect('blog_list')
    return render(request,'blog_form.html')

# Delete a blog post
def blog_delete(request,blog_id):
    blog = get_object_or_404(Blog, pk= blog_id)
    blog.delete()
    return redirect('blog_list')


def product_list(request):
    products = [
        {'name' : 'Laptop','price':1200},
        {'name' : 'Phone','price':800}
    ]
    return  render(request,'products.html',{'products':products})

