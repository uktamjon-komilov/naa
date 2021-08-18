from store.models import Product
from django.db import models
from django.contrib.auth import get_user_model

from store.models import ProductColor, ProductSize, SubCategory


def generate_coupon_code():
    import random
    import string

    available_chars = string.ascii_letters + string.digits
    code = ""

    for i in range(8):
        index = random.randint(0, len(available_chars)-1)
        code += available_chars[index]
    
    return code


def add_coupon(self):
    code = generate_coupon_code()
    coupons = Coupon.objects.filter(code=code)

    if not coupons.exists():
        coupon = Coupon(
            code=code,
            stock=self.stock,
            expires_in=self.expires_in
        )
        coupon.save()
        for category in self.category.all():
            print(category)
            coupon.category.add(category)
        coupon.save()
    else:
        add_coupon(self)


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

    reduced_price = models.FloatField(blank=True, default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        if self.reduced_price != 0.0:
            return self.reduced_price * self.quantity
        else:
            return self.product.price * self.quantity
    

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
    
    def get_price(self):
        if self.reduced_price != 0.0:
            return self.reduced_price
        else:
            return self.product.price


class Coupon(models.Model):
    code = models.CharField(max_length=8, blank=True, unique=True)
    stock = models.FloatField()
    expires_in = models.DateTimeField()
    category = models.ManyToManyField(SubCategory)
    is_used = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.code


class CouponGroup(models.Model):
    count = models.PositiveIntegerField()
    stock = models.FloatField()
    expires_in = models.DateTimeField()
    category = models.ManyToManyField(SubCategory)

        
    def save(self, *args, **kwargs):
        super(CouponGroup, self).save(*args, **kwargs)

        for _ in range(self.count):
            code = generate_coupon_code()
            coupons = Coupon.objects.filter(code=code)

            if not coupons.exists():
                coupon = Coupon(
                    code=code,
                    stock=self.stock,
                    expires_in=self.expires_in
                )
                coupon.save()
                coupon_group = CouponGroup.objects.get(count=self.count, stock=self.stock, expires_in=self.expires_in)
                print(coupon_group.category.all())
                coupon.category.add(*coupon_group.category.all())
                coupon.save()
            else:
                add_coupon(self)