from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart
from .tasks import order_created


def create_order(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()
            for item in cart:
                #fill in the items in the cart into the db
                OrderItem.objects.create(order = order, product=item['product'], price = item['price'], quantity=item['quantity'] )
            #clear the cart
            cart.clear()
            
            # launch asynchronous task to send mail
            order_created.delay(order.id)

            # set the order in the session
            request.session['order_id'] = order.id
            
            # redirect for payment
            return redirect(reverse('payment:process'))

            context = {
                'order' : order
            }
            return render(request, 'orders/order/created.html', context)
    else:
        form = OrderForm()
    context = {
        'cart': cart, 
        'form': form
    }

    return render(request,'orders/order/create.html', context)


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    context = {
        'order': order
    }
    return render(request,'admin/orders/order/detail.html',context)