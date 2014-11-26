import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
# Create your views here.

from books.models import Book

from books.forms import NewBookForm

class IndexView(View):
    """ Home page. """
    def get(self, request):
        books = Book.objects.filter(user=request.user)
        context = {'books': books}
        return render(request, 'books/index.html', context)

class ReadBookView(View):
    """ Read the contents of a book. """
    # TODO: books should be available at URL w/ slug instead of primary key
    #       or both options?
    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        context = {'book': book}
        return render(request, 'books/read_book.html', context)

class NewBookView(View):
    """ Page with a form to create a new book. """
    def get(self, request):
        context = {'form': NewBookForm()}
        return render(request, 'books/new_book.html', context)

    def post(self, request):
        form = NewBookForm(request.POST)
        if form.is_valid():
            # TODO: ModelForm?
            new_book = Book(user=request.user,
                            title=form.cleaned_data['title'],
                            url=form.cleaned_data['url'],
                            privacy=form.cleaned_data['privacy'],
                            pub_date=datetime.date.today())
            new_book.save()
            return redirect('edit_book', book_pk=new_book.id)
        else:
            context = {'form': form}
            return render(request, 'books/new_book.html', context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewBookView, self).dispatch(*args, **kwargs)

class EditBookView(View):
    """ Modify a book's settings and layout, but not content. """
    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        context = {'book': book}
        return render(request, 'books/edit_book.html', context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditBookView, self).dispatch(*args, **kwargs)

class WriteBookView(View):
    """ Modify a book's contents. """
    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        context = {'book': book}
        return render(request, 'books/write_book.html', context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WriteBookView, self).dispatch(*args, **kwargs)

