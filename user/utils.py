# helper function to help authenticate users 
# and also to clear any logic on the views

from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Vendor

def create_user_account(username, email, password, first_name="",
                        last_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        username=username, email=email,  first_name=first_name,
        last_name=last_name, password=password, **extra_fields)
    return user

def get_and_authenticate_user(username, password):
    # user = authenticate(username=email, password=password)
    user = authenticate(username=username, password=password)
    if user is None:
        res={
            "status": 401,
            "message":"invalid email/password, pleaser try again!"
        }
        raise serializers.ValidationError(res)

    return user


def create_vendor_account(username, email, password, first_name="",
                        last_name="", **extra_fields):
    print("username")
    print(email)
    print(password)
    vendor = Vendor.objects.create_user(
        username=username, email=email,  first_name=first_name,
        last_name=last_name, password=password, **extra_fields)
    return vendor