from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.home, name='home_category'),
    path('product/<int:id>/', views.product_details, name='product_details'),
]
