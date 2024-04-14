from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date', 'number_of_pages')
    list_filter = ('genre', 'publication_date')
    search_fields = ('title', 'author', 'genre', 'description')
    prepopulated_fields = {'slug': ('title',)}

    def get_ordering(self, request: HttpRequest) -> list[str] | tuple[Any, ...]:
        return super().get_ordering(request) or ['title']

admin.site.register(Book, BookAdmin) 