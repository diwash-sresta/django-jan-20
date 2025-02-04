from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Author

# def author(request):
#     authors = Author.objects.all()
#     return render(request,'demo.html',{'authors':authors})

def author_list(request):
    authors = Author.objects.all()
    return render(request,'author_list.html',{'authors':authors})

# View a single author post
def author_detail(request,author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request,'author_detail.html',{'author':author})

# Create a new author post
def author_create(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        Author.objects.create(name=name, email=email, age=age)
        return redirect('author_list')
    return render(request,'author_form.html')

# Delete a author post
def author_delete(request,author_id):
    author = get_object_or_404(Author, pk= author_id)
    author.delete()
    return redirect('author_list')
