from django.conf.urls import patterns, include, url

import books.views

urlpatterns = patterns('',
    url(r'^$', books.views.IndexView.as_view(), name='home'),
    url(r'^new-book/$', books.views.NewBookView.as_view(), name='new_book'),
    url(r'^(?P<book_pk>[0-9]+)/$', books.views.ReadBookView.as_view(), name='read_book'),
    url(r'^(?P<book_pk>[0-9]+)/edit/$', books.views.EditBookView.as_view(), name='edit_book'),
    url(r'^(?P<book_pk>[0-9]+)/write/$', books.views.WriteBookView.as_view(), name='write_book'),
    url(r'^(?P<book_pk>[0-9]+)/new-chapter/$', books.views.NewChapterView.as_view(), name='new_chapter'),
    url(r'^(?P<book_pk>[0-9]+)/(?P<chapter_pk>[0-9]+)/$', books.views.ReadChapterView.as_view(), name='read_chapter'),
    url(r'^(?P<book_pk>[0-9]+)/(?P<chapter_pk>[0-9]+)/edit/$', books.views.EditChapterView.as_view(), name='edit_chapter'),
    url(r'^(?P<book_pk>[0-9]+)/(?P<chapter_pk>[0-9]+)/write/$', books.views.WriteChapterView.as_view(), name='write_chapter'),
)

