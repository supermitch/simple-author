from django import forms

class NewBookForm(forms.Form):
    PRIVATE = 'private'
    PUBLIC = 'public'
    BOOK_PRIVACY_CHOICES = (
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    )
    title = forms.CharField(label="Book title", max_length=200)
    url = forms.SlugField()
    privacy = forms.ChoiceField(choices=BOOK_PRIVACY_CHOICES, initial=PUBLIC)
    # TODO: Image field for cover?

