from django.conf.urls import patterns, include, url

import books.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', books.views.IndexView.as_view(), name='home'),
    url(r'^new/$', books.views.NewBookView.as_view(), name='new_book'),
    url(r'^edit/(?P<book_pk>[0-9]+)/$$', books.views.EditBookView.as_view(), name='edit_book'),
    url(r'^write/(?P<book_pk>[0-9]+)/$$', books.views.WriteBookView.as_view(), name='write_book'),
    #url(r'^read/(?P<book_pk>[0-9]+)/$$', books.views.ReadBookView.as_view(), name='read_book'),
)

