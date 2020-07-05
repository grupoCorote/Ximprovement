from django.shortcuts import render
from rest_framework import viewsets
from frigobar.models.Product import Product
from frigobar.serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer