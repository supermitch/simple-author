from django.conf.urls import patterns, include, url

import books.views

urlpatterns = patterns('',
    url(r'^$', books.views.IndexView.as_view(), name='home'),
    url(r'^new-book/$', books.views.NewBookView.as_view(), name='new_book'),
    url(r'^book/(?P<book_pk>[0-9]+)/$', books.views.ReadBookView.as_view(), name='read_book'),
    url(r'^book/(?P<book_pk>[0-9]+)/edit/$', books.views.EditBookView.as_view(), name='edit_book'),
    url(r'^book/(?P<book_pk>[0-9]+)/write/$', books.views.WriteBookView.as_view(), name='write_book'),
    url(r'^book/(?P<book_pk>[0-9]+)/section/(?P<section_pk>[0-9]+)/$', books.views.ReadSectionView.as_view(), name='read_section'),
    url(r'^book/(?P<book_pk>[0-9]+)/section/(?P<section_pk>[0-9]+)/edit/$', books.views.EditSectionView.as_view(), name='edit_section'),
    url(r'^book/(?P<book_pk>[0-9]+)/section/(?P<section_pk>[0-9]+)/write/$', books.views.WriteSectionView.as_view(), name='write_section'),
)

