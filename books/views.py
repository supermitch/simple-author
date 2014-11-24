from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
# Create your views here.
from books.forms import NewBookForm

class IndexView(View):
    """ Home page. """
    def get(self, request):
        context = {'name': 'mitch'}
        return render(request, 'books/index.html', context)

class NewBookView(View):
    """ Page with a form to create a new book. """
    def get(self, request):
        context = {'form': NewBookForm()}
        return render(request, 'books/new_book.html', context)

    def post(self, request):
        form = NewBookForm(request.POST)
        if form.is_valid():
            # TODO: Create book record in DB
            print('Successfully created a book.')
            return redirect('edit_book', book_pk=1)
        else:
            context = {'form': form}
            return render(request, 'books/new_book.html', context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewBookView, self).dispatch(*args, **kwargs)

class EditBookView(View):
    """ Modify a book's settings and layout, but not content. """
    def get(self, request, book_pk):
        context = {'book_pk': book_pk}
        return render(request, 'books/edit_book.html', context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditBookView, self).dispatch(*args, **kwargs)

