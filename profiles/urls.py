from django.conf.urls import patterns, include, url

import profiles.views

urlpatterns = patterns('',
    # Edit your profile
    url(r'^edit/$', profiles.views.EditProfileView.as_view(), name='edit_profile'),
    # View a profile, including your own
    url(r'^(?P<author_name>[\w-]+)/$', profiles.views.ProfileView.as_view(), name='view_profile'),
)

