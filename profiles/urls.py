from django.conf.urls import patterns, include, url

import profiles.views

urlpatterns = patterns('',
    # View your own profile
    url(r'^$', profiles.views.ProfileView.as_view(), name='profile_home'),
    # Edit your profile
    url(r'^edit/$', profiles.views.EditProfileView.as_view(), name='edit_profile'),
    # View someone else's profile
#    url(r'^/(?P<author_name>[\w-]+)/$', books.views.NewChapterView.as_view(), name='view_profile'),
)

