from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    stock = models.IntegerField()
    price = models.FloatField(default=1000.0)
    date = models.DateField()



# User -> id, first_name, last_name, email, phone, password, is_active, is_admin, is_staff, is_superuser

# Product -> id, name, price, stock, description, rating, coupon, created_at, updated_at

# Category -> id, name, created_at, updated_at