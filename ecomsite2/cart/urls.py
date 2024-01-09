from django.urls import path
from . import views
urlpatterns = [
    path('add_product/<int:id>/', views.add_product, name='add_product'),
    path('remove_single_product/<int:id>/', views.remove_single_product, name='remove_single_product'),
    path('remove_product/<int:id>/', views.remove_product, name='remove_product'),
    path('cart/', views.cart, name='cart'),
    path('myorder/', views.make_order, name='make_order'),
]
