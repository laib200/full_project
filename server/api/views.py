from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Products
from products.serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class productViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
