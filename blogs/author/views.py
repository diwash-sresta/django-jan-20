from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
@login_required
def author_create(request):
    # Store the return URL
    return_url = request.GET.get('next', '/')
    
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            bio = request.POST.get('bio', '')
            email = request.POST.get('email', '')
            
            # Get return URL from form
            return_url = request.POST.get('next', return_url)
            
            if not name:
                messages.error(request, 'Author name is required.')
                return render(request, 'author/author_form.html', {'return_url': return_url})
            
            # Create the author
            author = Author.objects.create(
                user=request.user,
                name=name,
                bio=bio,
                email=email
            )
            
            # Force save to ensure the author is in the database
            author.save()
            
            messages.success(request, f'Author "{name}" created successfully!')
            
            # Print debug information
            print(f"Created new author: {author.name} (ID: {author.id})")
            print(f"Redirecting to: {return_url}")
            
            return redirect(return_url)
            
        except Exception as e:
            messages.error(request, f'Error creating author: {str(e)}')
            return render(request, 'author/author_form.html', {'return_url': return_url})
    
    return render(request, 'author/author_form.html', {'return_url': return_url})

# Delete a author post
def author_delete(request,author_id):
    author = get_object_or_404(Author, pk= author_id)
    author.delete()
    return redirect('author_list')
