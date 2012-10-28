from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    citizenship = models.CharField(_('citizenship'), max_length=30)
    biography = models.TextField(_('biography'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(_('name'), max_length=30)
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return self.name


class Editorial(models.Model):
    name = models.CharField(_('name'), max_length=30)
    city = models.CharField(_('city'), max_length=20, blank=True)
    address = models.CharField(_('address'), max_length=30, blank=True)
    website = models.URLField(_('website'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    isbn = models.IntegerField(unique=True)
    title = models.CharField(_('title'), max_length=30)
    price = models.FloatField(_('price'))
    description = models.TextField(_('description'), blank=True)
    picture = models.FileField(_('picture'), upload_to='media/')
    picture_path = models.FilePathField(_('picture path'), blank=True)
    quantity = models.IntegerField(_('quantity'))
    editorial = models.ForeignKey(Editorial)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    publication_date = models.DateField(_('publication date'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return self.title
