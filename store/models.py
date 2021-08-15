from django.db import models
from datetime import datetime, timezone
from django.conf import settings


class Category(models.Model):
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    name = models.CharField(max_length=255, verbose_name="Nomi")
    icon = models.ImageField(upload_to="images/", verbose_name="Rasmi")
    slug = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name



class SubCategory(models.Model):
    class Meta:
        verbose_name = "Kichik kategoriya"
        verbose_name_plural = "Kichik kategoriyalar"

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    title = models.CharField(max_length=255)
    price = models.FloatField()
    slug = models.CharField(max_length=255, null=True)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="images/")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    color = models.ManyToManyField(ProductColor)
    size = models.ManyToManyField(ProductSize)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.price}"
    

    def get_rating_percent(self):
        return 100 * (self.rating / 5)
    

    def is_new_product(self):
        time_delta = datetime.now(timezone.utc) - self.created_at
        return time_delta.seconds < settings.NEW_PRODUCT_SECONDS


class ProductImage(models.Model):
    image = models.ImageField(upload_to="images/", )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")



# for product in products:
#     product.title
#     product.description
#     for image in product.product_images:
#         print(image)