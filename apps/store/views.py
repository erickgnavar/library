from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


from inventory.models import *
from store.models import *


def cart_delete_book(request, item_id):
    if request.user.is_authenticated():
        user = request.user
        cart = Cart.objects.get(client=user.id, state='CC')
        item = Item.objects.get(pk=item_id)
        cart.items.remove(item)
        cart.save()
        item.delete()
    return HttpResponseRedirect('/carrito/')


def cart_add_book(request, book_id):
    if request.user.is_authenticated():
        user = request.user
        try:
            cart = Cart.objects.get(client=user.id, state='CC')
        except:
            cart = Cart(client=user, state='CC')
            cart.save()
        book = Book.objects.get(pk=book_id)
        item = Item(book=book)
        item.save()
        cart.items.add(item.id)
        cart.save()
    return HttpResponseRedirect('/')


def cart_list(request):
    message = ''
    if request.user.is_authenticated():
        client = request.user
        try:
            cart = Cart.objects.get(client__username=client.username)
            items = cart.items.all()
        except:
            cart = None
            items = None
    else:
        cart = None
        items = None
        message = 'No ha iniciado sesion'
    ctx = {
        'cart': cart,
        'items': items,
        'message': message
    }
    return render_to_response('store/cart_list.html', ctx, RequestContext(request))


def category_list(request, category_name):
    books_list = []
    for book in Book.objects.all():
        for category in book.categories.all():
            if category.name == category_name:
                books_list.append(book)

    paginator = Paginator(books_list, 1)

    page = 1
    if request.GET.get('page') is not None:
        page = request.GET['page']

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    ctx = {
        'books': books,
        'categories': Category.objects.all(),
        'active_category': category_name,
        'range': range(1, books.paginator.num_pages + 1)
    }
    return render_to_response('main/home.html', ctx, RequestContext(request))
