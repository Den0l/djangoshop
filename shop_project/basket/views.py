from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from basket.basket import Basket
from shop.models import Card, Pos_order
from .forms import *

def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Card, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')

@login_required
@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Card, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        count = form.cleaned_data['count']
        basket.add(
            product=product,
            count=count,
            update_count=form.cleaned_data['reload']
        )
    else:
        print(form.errors) 
    return redirect('basket_detail')

@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('base')
    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(
            buyer_firstname=form.cleaned_data['buyer_firstname'],
            buyer_name=form.cleaned_data['buyer_name'],
            buyer_surname=form.cleaned_data['buyer_surname'],
            comment=form.cleaned_data['comment'],
            delivery_address=form.cleaned_data['delivery_address'],
            delivery_type=form.cleaned_data['delivery_type'],
        )
        order.price = basket.get_total_price()
        for item in basket:
            pos_order = Pos_order.objects.create(
                cards=item['product'],
                order=order,
                count=item['count']
            )
        basket.clear()

    return redirect('basket_detail')

@login_required
def open_order(request):
    context = {
        'form_order': OrderForm
    }
    return render(request, 'order/order_form.html', context)