from django.urls import include, path
from .views import *

urlpatterns = [
    path('base', base_view, name='base'),
    path('about', about_view, name='about'),
    path('all_products', all_products_view, name='all_products'),
    path('cart', cart_view, name='cart'),
    path('categories', categories_view, name='categories'),
    path('contacts', contacts_view, name='contacts'),
    path('how_to_find', how_to_find_view, name='how_to_find'),
    path('index', index_view, name='index'),
    path('privacy', privacy_view, name='privacy'),
    path('product_detail', product_detail_view, name='product_detail'),
]
