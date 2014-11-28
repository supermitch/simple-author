import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View

from books.forms import NewBookForm, NewChapterForm
from books.models import Book, Chapter, Section

class IndexView(View):
    """ Home page. """
    def get(self, request):
        if request.user.is_authenticated():
            books = Book.objects.filter(user=request.user)
            context = {'books': books}
        else:
            context = {}
        return render(request, 'books/index.html', context)

class ReadBookView(View):
    """ Read the contents of a book. """
    # TODO: books should be available at URL w/ slug instead of primary key
    #       or both options?
    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        sections = Section.objects.filter(book=book)
        chapters = Chapter.objects.filter(book=book)
        context = {
            'book': book,
            'chapters': chapters,
            'sections': sections,
        }
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

class NewChapterView(View):
    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        # Find our current max order value
        max_order = Chapter.objects.filter(book_id=book_pk).aggregate(Max('order'))

        max_order = 0 if max_order.values()[0] is None else max_order.values()[0]
        new_order = max_order + 1
        new_name = 'Chapter ' + str(new_order)
        new_chapter = Chapter(book_id=book_pk, order=new_order, name=new_name)
        form = NewChapterForm(instance=new_chapter)

        context = {'book': book, 'form': form}
        return render(request, 'books/new_chapter.html', context)

    def post(self, request, book_pk):
        chapter = NewChapterForm(request.POST)
        if chapter.is_valid():
            chapter.save()  # Create new chapter
            # TODO: set new order?
            return redirect('new_chapter', book_pk=book_pk)
        else:
            context = {'book': book, 'form': chapter}
            return renter(request, 'books/new_chapter.html', context)


class EditBookView(View):
    """ Modify a book's settings and layout, but not content. """
    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        sections = Section.objects.filter(book=book)
        chapters = Chapter.objects.filter(book=book).order_by('order')
        context = {'book': book, 'sections': sections, 'chapters': chapters}

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

