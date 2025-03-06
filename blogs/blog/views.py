from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category, Author
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

@login_required
def blog_create(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            author_id = request.POST.get('author')
            author_name = request.POST.get('author_name')

            if not title or not content:
                messages.error(request, 'Title and content are required.')
                return redirect('blog:blog_create')

            # Get or create author
            if author_id:
                author = get_object_or_404(Author, id=author_id)
            else:
                author, created = Author.objects.get_or_create(user=request.user)
                if created and author_name:
                    author.name = author_name
                    author.save()

            blog = Blog.objects.create(
                title=title,
                content=content,
                author=author
            )

            messages.success(request, 'Blog post created successfully!')
            return redirect('blog:blog_detail', blog_id=blog.id)

        except Exception as e:
            messages.error(request, f'Error creating blog: {str(e)}')
            return redirect('blog:blog_create')

    authors = Author.objects.all().order_by('name')
    return render(request, 'blog_form.html', {'authors': authors})

@login_required
def blog_update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    
    # Check if user has permission to edit
    if blog.author.user != request.user and not request.user.is_staff:
        raise PermissionDenied("You don't have permission to edit this blog.")

    if request.method == "POST":
        try:
            blog.title = request.POST.get('title')
            blog.content = request.POST.get('content')
            author_id = request.POST.get('author')

            if author_id:
                blog.author = get_object_or_404(Author, id=author_id)

            blog.save()

            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog:blog_detail', blog_id=blog.id)

        except Exception as e:
            messages.error(request, f'Error updating blog: {str(e)}')
            return redirect('blog:blog_update', blog_id=blog_id)

    authors = Author.objects.all().order_by('name')
    return render(request, 'blog_form.html', {
        'blog': blog,
        'authors': authors
    })

@login_required
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    
    # Check if user has permission to delete
    if blog.author.user != request.user and not request.user.is_staff:
        raise PermissionDenied("You don't have permission to delete this blog.")

    if request.method == "POST":
        try:
            blog.delete()
            messages.success(request, 'Blog post deleted successfully!')
            return redirect('blog:blog_list')
        except Exception as e:
            messages.error(request, f'Error deleting blog: {str(e)}')
            return redirect('blog:blog_detail', blog_id=blog_id)

    return render(request, 'blog_confirm_delete.html', {'blog': blog})
