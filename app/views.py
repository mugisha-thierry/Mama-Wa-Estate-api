from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import EstateSerializer

from rest_framework import mixins, viewsets , generics
from .models import ProductMerch, Estate, Vendor
from .serializer import MerchSerializer, VendorSerializer

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
        all_vendors = Vendor.objects.all()
        serializers = VendorSerializer(all_vendors, many=True)
        return Response(serializers.data)