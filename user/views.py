from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


#local imports
from . import serializers
from .utils import get_and_authenticate_user, create_user_account, create_vendor_account

User = get_user_model()

class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer
    }


    @action(methods=['POST', 'GET'], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        serialized_data = serializers.AuthUserSerializer(user).data

        data = {
            "success": "Successfully registered proceed to login ",
            "status": status.HTTP_200_OK,
            "data":serialized_data
        }
        return Response(data, status=status.HTTP_201_CREATED)


    @action(methods=['POST', "GET"], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        serialized_data = serializers.AuthUserSerializer(user).data
        data = {
            "success": "Logged In sucesfully",
            "status": status.HTTP_200_OK,
            "data":serialized_data
        }
        return Response(data, status=status.HTTP_200_OK)


    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {
            "status":status.HTTP_200_OK,
            'success':'Successfully logged out'}
        return Response(data, status=status.HTTP_200_OK)


    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data.get('new_password'))
        request.user.save()
        res = {
            "status": status.HTTP_204_NO_CONTENT,
            "success": "Password has been changed"
        }
        return Response(res, status=status.HTTP_204_NO_CONTENT)
        

    # dynamically select serializers 
    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
           
class AuthVendors(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'vendor_login': serializers.VendorLoginSerializer,
        'vendor_register': serializers.VendorRegisterSerializer
    }

    @action(methods=['POST', 'GET'], detail=False)
    def vendor_register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("name")
       
        
        vendor = create_vendor_account(**serializer.validated_data)
        serialized_data = serializers.AuthVendorSerializer(vendor).data

        data = {
            "success": "Successfully registered proceed to login ",
            "status": status.HTTP_200_OK,
            "data":serialized_data
        }
        return Response(data, status=status.HTTP_201_CREATED)


    @action(methods=['POST', "GET"], detail=False)
    def vendor_login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vendor = get_and_authenticate_user(**serializer.validated_data)
        serialized_data = serializers.AuthUserSerializer(vendor).data
        data = {
            "success": "Logged In sucesfully",
            "status": status.HTTP_200_OK,
            "data":serialized_data
        }
        return Response(data, status=status.HTTP_200_OK)


    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {
            "status":status.HTTP_200_OK,
            'success':'Successfully logged out'}
        return Response(data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()