from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template import RequestContext


from inventory.models import Book, Category


def home(request):
    if request.GET.get('query') is not None:
        books_list = Book.objects.filter(title__icontains=request.GET['query'])
    else:
        books_list = Book.objects.all()
    paginator = Paginator(books_list, 3)

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
        'range': range(1, books.paginator.num_pages + 1)
    }
    return render_to_response('main/home.html', ctx, RequestContext(request))
