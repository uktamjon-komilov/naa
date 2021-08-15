from django.contrib import admin

# import admin_thumbnails

from .models import *


class ProductImageStackedAdmin(admin.StackedInline):
    model = ProductImage
    fields = ["image"]
    extra = 1



class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "rating", "sub_category", "is_active"]
    list_display_links = ["title"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}

    inlines = [ProductImageStackedAdmin]



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# @admin.register(ProductImage)
# @admin_thumbnails.thumbnail("image")
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ["image"]



admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductColor)
admin.site.register(ProductSize)

# admin.site.register(ProductImageAdmin)