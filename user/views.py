from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import UserProfile
from django.http import Http404
from rest_framework.views import APIView
from .models import UserProfile

#local imports
from . import serializers
from .utils import get_and_authenticate_user, create_user_account

User = get_user_model()


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer,
        'profile' :serializers.UserProfileSerializer
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

class ProfileSerializer(APIView):
    """
    List all profile, or create a new snippet.
    """
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    http_method_names = ['get', 'head', 'post']
    


    @action(methods=['POST', 'GET'], detail=False, permission_classes=[IsAuthenticated, ])
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        
        data = {
            "success": "Your profile has been Successfully updated ",
    
            # "data":serialized_data
        }
        # return Response(data, status=status.HTTP_201_CREATED)
       

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

