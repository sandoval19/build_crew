from rest_framework import serializers
from apps.products.models.products import Products


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'code',
            'category',
            'name',
            'quantity',
            'price',
            'bill_id',
            'is_active'
        ]


class ProductsPatchSerializer(serializers.ModelSerializer):
    class Meta():
        model = Products
        fields = [
            "category",
            "name",
            "price",
            "quantity",
            'is_active',
        ]
