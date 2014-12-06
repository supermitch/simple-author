from django.contrib import admin

import books.models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'website')
admin.site.register(books.models.Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'pub_date')
admin.site.register(books.models.Book, BookAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_filter = ['location']
    list_display = ('kind', 'location')
    ordering = ['-location', ]
admin.site.register(books.models.Section, SectionAdmin)

class BookSectionsAdmin(admin.ModelAdmin):
    list_display = ('book', 'section', 'content')
    ordering = ['book', 'section']
admin.site.register(books.models.BookSections, BookSectionsAdmin)


