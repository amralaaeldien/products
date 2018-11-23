from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from products_and_categories.models import Product, Category
from products_and_categories.serializers import ProductSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer