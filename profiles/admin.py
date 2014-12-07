from django.contrib import admin

# Register your models here.
import profiles.models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'website', 'privacy')
admin.site.register(profiles.models.Author, AuthorAdmin)


