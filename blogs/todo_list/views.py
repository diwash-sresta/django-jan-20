from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task

def todo_list(request):
    tasks = Task.objects.all()
    return render(request,'todo_list.html',{'tasks':tasks})

def todo_detail(request,todo_id):
    task = get_object_or_404(Task, pk=todo_id)
    return render(request,'todo_detail.html',{'task':task})

def todo_create(request):
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     Task.objects.create(title=title)
    #     return redirect('todo_list')
    # return render(request,'todo_form.html')
    if request.method == "POST":
        title = request.POST.get('title')
        completed = request.POST.get('completed') == 'on'  # If checkbox is checked, task is completed
        Task.objects.create(title=title, completed=completed)
        return redirect('todo_list')  # Redirect to the todo list page

    tasks = Task.objects.all()  # Retrieve all tasks
    return render(request, 'todo_form.html', {'tasks': tasks})
def todo_delete(request,todo_id):
    task = get_object_or_404(Task, pk=todo_id)
    task.delete()
    return redirect('todo_list')


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle status
    task.save()
    return redirect('todo_list')  # Redirect back to the list

def clear_tasks(request):
    Task.objects.all().delete()  # Delete all tasks
    return redirect('todo_list')
