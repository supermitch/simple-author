from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView

from books.models import Author

class ProfileView(View):
    """ Display a profile defined by the author_name. """
    def get(self, request, author_name):
        author = get_object_or_404(Author, author_name=author_name)
        context = {
            'author': author,
        }
        return render(request, 'profiles/view_profile.html', context)

class EditProfileView(TemplateView):
    template_name = 'profiles/edit_profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditProfileView, self).dispatch(*args, **kwargs)

