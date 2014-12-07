from django.conf.urls import patterns, include, url

import profiles.views

urlpatterns = patterns('',
    # View your profile
    url(r'^$', profiles.views.ProfileView.as_view(), name='view_profile'),
    # View a specific profile
    url(r'^(?P<display_name>[\w-]+)/$', profiles.views.ProfileView.as_view(), name='view_profile'),
    # Edit your profile
    url(r'^edit/$', profiles.views.EditProfileView.as_view(), name='edit_profile'),
)

