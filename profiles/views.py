from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView

from books.models import Author

class ProfileView(View):
    """ Display a profile defined by the author_name. """
    def get(self, request, display_name):
        if request.user.is_authenticated() and \
            request.user.author.display_name == display_name:
                # We're looking at our own profile
                author = request.user.author
        else:
            # We can only see public profiles
            author = get_object_or_404(Author, display_name=display_name,
                                       privacy='public')
        context = {
            'author': author,
        }
        return render(request, 'profiles/view_profile.html', context)

class EditProfileView(View):
    template_name = 'profiles/edit_profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditProfileView, self).dispatch(*args, **kwargs)

