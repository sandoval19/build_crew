from django.contrib import admin
from apps.products.models.products import Products
from apps.products.models.category import Category


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'category',
        'name',
        'quantity',
        'price'
    )
    list_filter = (
    'code',
    'category',
    )
    search_fields = (
    'name',
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = (
        'name',
    )

