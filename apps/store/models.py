from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from inventory.models import Book

CART_STATES = (
    ('CC', _('Created Cart')),
    ('SC', _('Paid Cart')),
    ('DC', _('Delivered Cart'))
)


class Item(models.Model):
    book = models.ForeignKey(Book)
    quantity = models.IntegerField(_('quantity'), default=1)
    discount_rate = models.FloatField(_('discount rate'), default=0)
    discount_amount = models.FloatField(_('discount amount'), default=0)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return '%s - %i' % (self.book.title, self.quantity)


class Cart(models.Model):
    items = models.ManyToManyField(Item)
    subtotal = models.FloatField(_('subtotal'), default=0)
    total = models.FloatField(_('total'), default=0)
    state = models.CharField(_('state'), max_length=2, choices=CART_STATES)
    client = models.ForeignKey(User)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return '%i items' % (len(self.items.all()))
