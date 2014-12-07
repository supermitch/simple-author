from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView

import profiles.models
from profiles.models import Author

class ProfileView(View):
    """ Display a profile defined by the author_name. """
    def get(self, request, display_name=None):
        if display_name is None:
            # If we're logged in, get our own profile
            if request.user.is_authenticated():
                try:
                    author = request.user.author
                except ObjectDoesNotExist:
                    # Our profile is blank, so let's create one:
                    author = Author(user=request.user,
                                    display_name=request.user.username)
                    author.save()
            else:
                raise Http404
        else:
            # We can only see profiles that are public
            author = get_object_or_404(Author, display_name=display_name,
                                       privacy=profiles.models.PUBLIC)

        if request.user.is_authenticated() and request.user == author.user:
            viewing_self = True
        else:
            viewing_self = False
        context = {
            'author': author,
            'viewing_self': viewing_self,
        }
        return render(request, 'profiles/view_profile.html', context)

class EditProfileView(View):
    template_name = 'profiles/edit_profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditProfileView, self).dispatch(*args, **kwargs)

