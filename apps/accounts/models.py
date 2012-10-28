from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


SEX = (
    ('M', 'male'),
    ('F', 'female')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(_('gender'), max_length=1, choices=SEX)
