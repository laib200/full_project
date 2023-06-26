from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import productViewSet
from api import auth
routers = DefaultRouter()
auth_routers = DefaultRouter()
routers.register('products', productViewSet, 'products')
auth_routers.register('register', auth.Register, 'register')
auth_routers.register('login', auth.Login, 'login')

urlpatterns = [
    path('', include(routers.urls)),
    path('auth/', include(auth_routers.urls))
]
