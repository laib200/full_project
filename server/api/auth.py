from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializer import UserAuthSerializer
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


class Register(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


class Login(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        except:
            return Response({"username": ["A user with that username not exists."]}, status=status.HTTP_400_BAD_REQUEST)
