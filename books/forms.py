from django import forms

from books import models

class NewBookForm(forms.Form):
    """ Add a new book. """
    # TODO: ModelForm?
    title = forms.CharField(label="Book title", max_length=200)
    url = forms.SlugField()
    privacy = forms.ChoiceField(choices=models.Book.PRIVACY_CHOICES,
                                initial=models.Book.PUBLIC)
    # TODO: Image field for cover?

class NewChapterForm(forms.ModelForm):
    """ Add a new chapter to a book. """
    class Meta:
        model = models.Chapter
        fields = ['book', 'name', 'order']
        widgets = {'book': forms.HiddenInput()}

def verify_sections(CheckBoxInput):
    print(CheckBoxInput)
    return True

class SelectFrontMatterForm(forms.Form):
    sections = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=models.FRONT_MATTER_CHOICES,
        label='Front Matter')

class SelectBackMatterForm(forms.Form):
    sections = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=models.BACK_MATTER_CHOICES,
        label='Back Matter')

