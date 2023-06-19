from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import productViewSet
routers = DefaultRouter()
routers.register('products', productViewSet,'products')

urlpatterns = [
    path('',include(routers.urls))
]
