from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","created_at","updated_at")
    search_fields = ("title"),


admin.site.register(Blog,BlogAdmin)
