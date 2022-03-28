from django.contrib import admin
from .models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", 'theme', "author", "cover")
    prepopulated_fields = {"slug": ("title",)}
