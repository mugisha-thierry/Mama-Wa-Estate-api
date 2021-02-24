from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import User, UserProfile


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    serializer for registering a user
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

        def validate_email(self, value):
            user = User.objects.filter(email=email)
            if user:
                raise serializers.ValidationError("Email is already taken")
            return BaseUserManager.normalize_email(value)

        def  validate_password(self, value):
            password_validation.validate_password(value)
            return value


class UserLoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    username = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'auth_token')
         read_only_fields = ('id', 'is_active', 'is_staff')
    
    def get_auth_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key


class EmptySerializer(serializers.Serializer):
    pass

    
class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

class UserProfileSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)
    class Meta:
        model = UserProfile
        fields = ('bio', 'dob', 'location', 'country', 'city', 'zip', 'photo')


    


       
    