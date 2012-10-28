from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.home'),
    url(r'^ingresar/$', 'accounts.views.login_user', name='login'),
    url(r'^salir/$', 'accounts.views.logout_user', name='logout'),
    url(r'^registrar/$', 'accounts.views.register_user', name='register'),
    url(r'^micuenta/$', 'accounts.views.user_detail', name='profile'),
    url(r'^libro/(?P<book_id>\d+)?$', 'inventory.views.book_detail', name='book_detail'),
    url(r'^categoria/(?P<category_name>\w+)/$', 'store.views.category_list', name='category'),
    url(r'^carrito/$', 'store.views.cart_list', name='shopping_cart'),
    url(r'^carrito/agregar/(?P<book_id>\d+)/$', 'store.views.cart_add_book', name='cart_add_book'),
    url(r'^carrito/borrar/(?P<item_id>\d+)/$', 'store.views.cart_delete_book', name='cart_delete_book'),
    # url(r'^library/', include('library.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
