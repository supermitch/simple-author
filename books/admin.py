from django.contrib import admin

import books.models

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'view_mode', 'show_toc', 'pub_date')
admin.site.register(books.models.Book, BookAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_filter = ['location', 'multiple']
    list_display = ('kind', 'initial_order', 'multiple', 'location')
    ordering = ['initial_order']
admin.site.register(books.models.Section, SectionAdmin)

class BookSectionsAdmin(admin.ModelAdmin):
    list_display = ('book', 'name', 'order', 'section')
    list_display_links = ('book', 'name', 'section')
    ordering = ['book', 'order', 'name']
admin.site.register(books.models.BookSections, BookSectionsAdmin)


