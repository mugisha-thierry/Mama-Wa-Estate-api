from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializer import EstateSerializer
from .forms import StoreForm


from rest_framework import mixins, viewsets , generics
from .models import ProductMerch, Estate, Vendor, Store
from .serializer import MerchSerializer, VendorSerializer, StoreSerializer

# Create your views here.


class Estate(APIView):
    def get(self, request, format=None):
        all_estate = Estate.objects.all()
        serializers = EstateSerializer(all_estate, many=True)
        return Response(serializers.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = ProductMerch.objects.all()
    serializer_class = MerchSerializer

class VendorsList(APIView):
    def get(self, request, format=None):
        permission_classes = [IsAuthenticated]
        all_vendors = Vendor.objects.all()
        serializers = VendorSerializer(all_vendors, many=True)
        return Response(serializers.data)

class StoresList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        all_stores = Store.objects.all()
        serializers = StoreSerializer(all_stores, many=True)
        return Response(serializers.data)

    def set(self, request, format=None):
        request.method = 'POST'
        all_stores = Store.objects.all()
        serializers = StoreSerializer(all_stores, many=True)
        return Response(data)