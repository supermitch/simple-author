from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'author.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('books.urls')),
)
