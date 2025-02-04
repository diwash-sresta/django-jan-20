from django.contrib import admin

from .models import Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","published_at","author")
    search_fields = ("title"),


admin.site.register(Post,BlogAdmin)
