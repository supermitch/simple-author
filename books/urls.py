from django.conf.urls import patterns, include, url

from books.views import IndexView, NewBookView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^new/$', NewBookView.as_view(), name='new_book'),
    url(r'^edit/(?P<book>[0-9]+)/$$', EditBookView.as_view(), name='edit_book'),
)

