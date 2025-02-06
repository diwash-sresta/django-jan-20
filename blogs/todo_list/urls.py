from django.urls import path
from .import views

urlpatterns = [
    path('',views.todo_list, name='todo_list'),
    path('<int:todo_id>/',views.todo_detail, name='todo_detail'),
    path('add/',views.todo_create, name='todo_create'),
    path('<int:todo_id>/delete/',views.todo_delete, name='todo_delete'),
    path('<int:task_id>/toggle/', views.toggle_task, name='toggle_task'),
    path('clear/', views.clear_tasks, name='clear_tasks'),
]