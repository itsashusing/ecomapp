from django.shortcuts import render, redirect
from .models import Cart, OrderItem, Orders
from store.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.


def cart_id(request):
    id = request.session.session_key
    if not id:
        id = request.session.create()
    return id


def add_product(request, id):
    product = Product.objects.get(id=id)

    try:
        cart = Cart.objects.get(name=cart_id(request))

    except:
        cart = Cart.objects.create(
            name=cart_id(request)
        )
        cart.save()

    try:
        cart_item = OrderItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except:
        cart_item = OrderItem.objects.create(
            cart=cart,
            product=product,
            quantity=1
        )
        cart_item.save()
    return redirect('cart')


def remove_single_product(request, id):
    product = Product.objects.get(id=id)
    cart_item = OrderItem.objects.get(product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_product(request, id):
    product = Product.objects.get(id=id)
    cart_item = OrderItem.objects.get(product=product)
    cart_item.delete()
    return redirect('cart')


def cart(request):
    cart_items = OrderItem.objects.filter(cart__name=cart_id(request))

    total = 0
    for price in cart_items:
        total += price.total_price()

    context = {
        'cart_items': cart_items,
        'total': total

    }
    return render(request, 'cart/cart.html', context)


# making orders
@login_required
def make_order(request):
    try:
        if request.POST.get('order'):
            items = OrderItem.objects.all()

            t_quan = 0
            price = 0
            for item in items:
                t_quan = t_quan+item.quantity
                price = price+item.total_price()

            for item in items:
                order = Orders.objects.create(
                    product=item.product,
                    category=item.product.category,
                    quantity=t_quan,
                    price=price,
                    user=request.user
                )
                order.save()
                item.delete()
    except:
        return redirect('make_order')
    try:
        order_list = Orders.objects.all().filter(user=request.user)
    except:
        order_list = None
    context = {
        'order_list': order_list
    }
    return render(request, 'store/myorder.html', context)
