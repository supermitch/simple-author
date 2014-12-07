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
    display_name = models.SlugField(max_length=50, blank=True, unique=True)
    website = models.URLField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    privacy = models.CharField(max_length=10, choices=PRIVACY,
                               default=PUBLIC)
    def __str__(self):
        return self.user.username

