from store.models import Product
from django.db import models
from django.contrib.auth import get_user_model

from store.models import ProductColor, ProductSize


User = get_user_model()


class Cart(models.Model):
    session_id = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    color = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=255, null=True)
    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return self.quantity * self.product.price
    

    def get_color_name(self):
        color = ProductColor.objects.filter(id=int(self.color)).first()
        if color:
            return color.name
        else:
            return None
        
    def get_size_name(self):
        size = ProductSize.objects.filter(id=int(self.size)).first()
        if size:
            return size.name
        else:
            return None

