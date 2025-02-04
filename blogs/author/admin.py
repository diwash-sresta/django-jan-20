from django.contrib import admin

from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","email","age","created_at","updated_at")
    search_fields = ("name"),

admin.site.register(Author,AuthorAdmin)

