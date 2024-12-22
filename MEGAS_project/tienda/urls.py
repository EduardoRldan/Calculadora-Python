from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tienda/', views.inicio, name='inicio_tienda'),
    path('productos/', views.product_list, name='product_list'),
    path('producto/<int:pk>/', views.product_detail, name='product_detail'),
    path('carrito/', views.cart_view, name='cart_view'),
    path('carrito/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('ordenes/', views.order_list, name='order_list'),
]
