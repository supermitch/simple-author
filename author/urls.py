from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('books.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('profiles.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

