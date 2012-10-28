from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from inventory.models import *


def home(request):
    return render_to_response('main/home.html')


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    ctx = {
        'book': book
    }
    return render_to_response('inventory/book_detail.html', ctx, RequestContext(request))
