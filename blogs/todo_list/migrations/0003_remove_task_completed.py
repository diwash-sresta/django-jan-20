# Generated by Django 5.1.5 on 2025-02-04 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_task_delete_todo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]
