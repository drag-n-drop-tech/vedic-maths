from django.shortcuts import render
from rest_framework import viewsets, permissions


from .serializer import ProductsSerializer, Product_categorySerializer
from .models import Product_category, Products



class productsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = Product_category.objects.all()
    serializer_class = Product_categorySerializer

    
