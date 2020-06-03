from django.shortcuts import render
from .models import OrderItem
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
            # launch asynchronous task
            order_created.delay(order.id)
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
