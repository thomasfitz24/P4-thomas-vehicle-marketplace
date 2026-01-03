from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "price", "year", "is_available")
    list_filter = ("is_available", "category")
    search_fields = ("name", "description")

    fields = (
        "name",
        "slug",
        "category",
        "price",
        "year",
        "mileage",
        "image",
        "description",
        "is_available",
    )
