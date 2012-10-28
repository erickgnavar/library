from django.contrib import admin

from models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'citizenship', 'biography', 'created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')


class EditorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'address', 'website', 'created_at', 'updated_at')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'title', 'price', 'description', 'picture', 'picture_path', 'quantity', 'publication_date', 'editorial', 'created_at', 'updated_at')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Book, BookAdmin)
