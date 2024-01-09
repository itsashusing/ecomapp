from django.shortcuts import render
from .models import Product
from cart.views import cart_id
from django.core.paginator import Paginator
# Create your views here.


def home(request,id=None):
    if id:
        products=Product.objects.all().filter(category__id=id)
    else:
        products = Product.objects.all().order_by('?')
    # checking session
    p=cart_id(request)
    print(request.user)
    # -------------

    paginator =Paginator(products,4)
    page_number = request.GET.get("page")
    page_obj = paginator .get_page(page_number)

    context = {
        'products': products,
        'page_obj':page_obj
    }
    return render(request, 'store/home.html', context)


def product_details(request, id):
    product = Product.objects.get(id=id)
    side_products=Product.objects.all().order_by('?')

    context = {
        'product': product,
        'side_products':side_products[:4:]
    }
    return render(request, 'store/product_details.html', context)


