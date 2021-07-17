from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


class Category(models.Model):
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


    name = models.CharField(verbose_name="Nomi", max_length=255)
    icon = models.ImageField(upload_to="images/", null=True)
    
    created_at = models.DateTimeField(verbose_name="Yaratilgan sana", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="O'zgartirilgan sana", auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    product_description = models.TextField()
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
