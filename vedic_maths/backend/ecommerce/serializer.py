from rest_framework import serializers
from .models import Product_category, Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class Product_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_category
        fields = '__all__'



