from django.contrib import admin

from books.models import Author
from books.models import Book
from books.models import Chapter

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Chapter)

