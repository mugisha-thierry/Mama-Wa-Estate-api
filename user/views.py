from django.shortcuts import render
from rest_framework import generics, permissions,status
from django.contrib.auth.models import User
# from knox.models import AuthToken
from rest_framework.views import APIView
# from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from  .serializers import UserSerializer, RegisterSerializer, AuthTokenSerializer
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class UserSerializer(viewsets.ModelViewSet):
    # api endpoint that allows users to be viewed or edited
    queryset = User.objects.all().order_by()
    serializer_class = UserSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context).data,
        # "token": AuthToken.objects.create(user)[1]
        })   

class LoginAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None) 

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user                
