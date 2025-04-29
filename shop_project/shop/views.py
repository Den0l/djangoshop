from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request, 'base.html')

def about_view(request):
    return render(request, 'about.html')

def all_products_view(request):
    return render(request, 'all_products.html')

def cart_view(request):
    return render(request, 'cart.html')

def categories_view(request):
    return render(request, 'categories.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def how_to_find_view(request):
    return render(request, 'how_to_find.html')

def index_view(request):
    return render(request, 'index.html')

def privacy_view(request):
    return render(request, 'privacy.html')

def product_detail_view(request):
    return render(request, 'product_detail.html')