from django import forms

from books.models import Book  # Import choices for form

class NewBookForm(forms.Form):
    # TODO: ModelForm?
    title = forms.CharField(label="Book title", max_length=200)
    url = forms.SlugField()
    privacy = forms.ChoiceField(choices=Book.PRIVACY_CHOICES,
                                initial=Book.PUBLIC)
    # TODO: Image field for cover?

