from django.contrib.auth.models import User
from django.db import models

PRIVATE = 'Private'
PUBLIC = 'Public'
PRIVACY = (
    (PRIVATE, 'Private'),
    (PUBLIC, 'Public'),
)

class Author(models.Model):
    """ Extend the User model w/ Author information. """
    user = models.OneToOneField(User)
    # user.username is never displayed. Display_name is.
    display_name = models.SlugField(max_length=50, blank=True, unique=True)
    website = models.URLField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    # Profile privacy
    privacy = models.CharField(max_length=9, choices=PRIVACY,
                               default=PUBLIC)
    # Allow email to be displayed, specifically
    public_email = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

