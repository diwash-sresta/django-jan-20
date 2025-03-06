from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from author.models import Author

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create and log in the user
            user = form.save()
            
            # Create author profile
            Author.objects.create(
                user=user,
                name=user.username
            )
            
            # Log in the user
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to My Blog.')
            return redirect('blog:blog_list')
        else:
            # Show form errors
            for error in form.errors.values():
                messages.error(request, str(error))
    
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
