from django.contrib import admin

from books.models import Book, Chapter
# Register your models here.

admin.site.register(Book)
admin.site.register(Chapter)

