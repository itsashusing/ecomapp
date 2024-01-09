from .models import OrderItem
from store.models import Category


def count(request):
    order_count = OrderItem.objects.filter(
        cart__name=request.session.session_key).count()
    return dict(order_count=order_count)


def category(request):
    cat = Category.objects.all()

    return dict(cat=cat)
