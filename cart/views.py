from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .form import AddProductToCartForm
from coupons.forms import CouponApplyForm

# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)

    form = AddProductToCartForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product, quantity=cd['quantity'], override_quantity=cd['override'])

    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    
    for item in cart:
        item['update_quantity_form'] = AddProductToCartForm(initial={'quantity': item['quantity'], 'override': True})

    coupon_apply_form = CouponApplyForm()

    context = {
        'cart': cart,
        'coupon_apply_form' : coupon_apply_form

    }

    return render(request, 'cart/cart.html', context)


