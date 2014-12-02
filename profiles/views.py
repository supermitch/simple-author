from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView

class ProfileView(TemplateView):
    template_name = 'profiles/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)

class EditProfileView(TemplateView):
    template_name = 'profiles/edit_profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditProfileView, self).dispatch(*args, **kwargs)

