# Generated by Django 5.1.5 on 2025-01-31 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_2', '0003_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
