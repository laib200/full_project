from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Products
from products.serializers import ProductSerializer
# Create your views here.

class productViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
