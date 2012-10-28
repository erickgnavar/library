from django.contrib import admin
from store.models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'quantity', 'discount_rate', 'discount_amount', 'created_at', 'updated_at')


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'subtotal', 'total', 'state', 'client', 'created_at', 'updated_at')


admin.site.register(Item, ItemAdmin)
admin.site.register(Cart, CartAdmin)
