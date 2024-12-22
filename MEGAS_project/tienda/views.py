from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ShoppingCart, ShoppingCartItem

def inicio(request):
    return render(request, 'tienda/inicio.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'tienda/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'tienda/product_detail.html', {'product': product})

def cart_view(request):
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    items = ShoppingCartItem.objects.filter(cart=cart)
    return render(request, 'tienda/cart_view.html', {'items': items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    cart_item, created = ShoppingCartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_view')

def order_list(request):
    pass
