import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View

import books.forms
from books.forms import NewBookForm, NewChapterForm
import books.models
from books.models import Book, Chapter, Section, BookSections

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
        #sections = Section.objects.filter(book=book)
        chapters = Chapter.objects.filter(book=book)
        context = {
            'book': book,
            'chapters': chapters,
        #    'sections': sections,
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

    def add_checked(self, book, location, submitted_section_names):
        """ Add a relationship for check sections. """
        for section_name in submitted_section_names:
            section = Section.objects.get(name=section_name, location=location)
            if section not in book.sections.all():  # Don't re-add
                book_sect = BookSections(book=book, section=section)
                book_sect.save()

    def clear_unchecked(self, book, location, submitted_section_names):
        """ Remove any sections that were unchecked. """
        current_sections = Section.objects.filter(book=book, location=location)
        for section in current_sections:
            if section.name not in submitted_section_names:
                book_sect = BookSections.objects.get(book=book,
                                                     section=section)
                book_sect.delete()  # TODO: Hide only?

    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        chapters = Chapter.objects.filter(book=book).order_by('order')

        book_matter = book.sections.all()

        initial_front_matter = [section.name for section in book_matter \
                                if section.location == 'front']
        front_form = books.forms.SelectFrontMatterForm(
            initial={'sections': initial_front_matter})

        initial_back_matter = [section.name for section in book_matter \
                               if section.location == 'back']
        back_form = books.forms.SelectBackMatterForm(
            initial={'sections': initial_back_matter})

        context = {'book': book,
            'chapters': chapters,
            'front_form': front_form,
            'back_form': back_form,
        }

        return render(request, 'books/edit_book.html', context)

    def post(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)

        front_matter_form = books.forms.SelectFrontMatterForm(request.POST)
        back_matter_form = books.forms.SelectBackMatterForm(request.POST)

        if front_matter_form.is_valid():
            location = 'front'
            submitted_section_names = front_matter_form.cleaned_data['sections']
            self.clear_unchecked(book, location, submitted_section_names)
            self.add_checked(book, location, submitted_section_names)

            return redirect('edit_book', book_pk=book_pk)

        elif back_matter_form.is_valid():
            location = 'back'
            submitted_section_names = back_matter_form.cleaned_data['sections']
            self.clear_unchecked(book, location, submitted_section_names)
            self.add_checked(book, location, submitted_section_names)

            return redirect('edit_book', book_pk=book_pk)
        else:
            context = {'book': book}
            return renter(request, 'books/edit_book.html', context)


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

