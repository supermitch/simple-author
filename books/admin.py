from django.contrib import admin

import books.models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'website')
admin.site.register(books.models.Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
admin.site.register(books.models.Book, BookAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_type', 'book')
admin.site.register(books.models.Section, SectionAdmin)

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'order')
admin.site.register(books.models.Chapter, ChapterAdmin)


