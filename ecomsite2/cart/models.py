from django.db import models
from store.models import Product,Category
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

status_r=(
    ('pending','pending'),
    ('confirm','confirm'),
    ('deliverd','deliverd')
)

class Cart(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product}----{self.quantity}'

    def total_price(self):
        return self.quantity * self.product.sub_price()

class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.IntegerField()
    status=models.CharField(choices=status_r,max_length=10,default='pending')
