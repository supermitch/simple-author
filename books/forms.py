from django import forms

from books import models

from django.forms.models import modelformset_factory

BookSectionFormSet = modelformset_factory(models.BookSections,
    fields=('section', 'name', 'order'))

class NewBookForm(forms.Form):
    """ Add a new book. """
    # TODO: ModelForm?
    title = forms.CharField(label="Book title", max_length=200)
    url = forms.SlugField()
    privacy = forms.ChoiceField(choices=models.PRIVACY,
                                initial=models.PUBLIC)
    # TODO: Image field for cover?

class NewSectionForm(forms.ModelForm):
    """ Add a new section to a book. """
    class Meta:
        fields = ['book', 'name', 'order']
        widgets = {'book': forms.HiddenInput()}

class WriteBookSectionForm(forms.ModelForm):
    """ Writing content requires a form. """
    class Meta:
        model = models.BookSections
        fields = ['name', 'content']

def verify_sections(CheckBoxInput):
    print(CheckBoxInput)
    return True

class SelectFrontMatterForm(forms.Form):
    sections = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=models.FRONT_MATTER,
        label='Front Matter')

class SelectBackMatterForm(forms.Form):
    sections = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=models.BACK_MATTER,
        label='Back Matter')

