from django.contrib import admin
from .models import Cart,OrderItem,Orders
# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display=['product','category','quantity','date','user','price','status']

admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Orders,OrdersAdmin)