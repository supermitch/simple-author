from django import forms

import books

class EditProfileForm(forms.Form):
    """ Edit author and user settings. """
    first_name = forms.CharField(max_length=200, null=True, blank=True)
    last_name = forms.CharField(max_length=200, null=True, blank=True)
    email = forms.EmailField(null=True, blank=True)
    privacy = forms.ChoiceField(label="Profile privacy",
                                choices=books.models.Book.PRIVACY_CHOICES,
                                initial=books.models.Book.PUBLIC)
    website = forms.URLField(help_text="Your website", blank=True, null=True)
    bio = form.TextField(blank=True, null=True)
    # TODO: Image field for profile?

