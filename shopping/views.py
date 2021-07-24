from django.shortcuts import redirect, render
from django.urls import reverse

from store.models import Product
from .models import Cart, CartItem


def get_cart(request):
    session_id = request.session.session_key
    if session_id:
        session_id = request.session.create()
    
    cart = Cart.objects.filter(session_id=session_id)
    if cart.exists():
        cart = cart.first()
    else:
        cart = Cart(session_id=session_id).save()
    
    return cart


def add_cartitem(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect(reverse("home-page"))

    cart = get_cart(request)
    try:
        cartitem = CartItem.objects.get(cart=cart, product=product)
        cartitem.quantity += 1
    except CartItem.DoesNotExist:
        cartitem = CartItem(product=product, cart=cart)

    cartitem.save()

    return redirect(reverse("cart"))


def subtract_cartitem(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect(reverse("home-page"))

    cart = get_cart(request)
    try:
        cartitem = CartItem.objects.get(cart=cart, product=product)
        if cartitem.quantity > 1:
            cartitem.quantity -= 1
            cartitem.save()
        else:
            cartitem.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect(reverse("cart"))


def remove_cartitem(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect(reverse("home-page"))

    cart = get_cart(request)
    try:
        cartitem = CartItem.objects.get(cart=cart, product=product)
        cartitem.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect(reverse("cart"))


def cart(request):
    cart = get_cart(request)
    cartitems = CartItem.objects.filter(cart=cart)
    context = {
        "cartitems": cartitems
    }
    return render(request, "cart.html", context)