from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializer import EstateSerializer
from .forms import StoreForm
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework import mixins, viewsets , generics
from .models import ProductMerch, Estate, Vendor, Store, Category
from .serializer import MerchSerializer, VendorSerializer, StoreSerializer
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Estate,ProductMerch,Vendor
from .serializer import EstateSerializer,CategorySerializer,MerchSerializer,VendorSerializer
from rest_framework import mixins, viewsets , generics, status


from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView

# Create your views here.

class EstateView(APIView):
    name = "estate"
    def get(self, request, format=None):
        all_estate = Estate.objects.all()
        serializers = EstateSerializer(all_estate, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers =  EstateSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)        



class CategoryView(APIView):
    name = "category"
    def get(self, request, format=None):
        all_category = Category.objects.all()
        serializers =CategorySerializer(all_category, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers =  CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)        


class PostViewSet(viewsets.ModelViewSet):
    name = "products"
    queryset = ProductMerch.objects.all()
    serializer_class = MerchSerializer

class VendorsList(APIView):
    name = "vendors"
    def get(self, request, format=None):
        
        all_vendors = Vendor.objects.all()
        serializers = VendorSerializer(all_vendors, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        permission_classes = [IsAuthenticated]
        serializers = VendorSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StoresList(APIView):
    name = 'stores'
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        all_stores = Store.objects.all()
        serializers = StoreSerializer(all_stores, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = StoreSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,  status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def storeDetail(request, pk):
    name = 'store-detail'
    store = Store.objects.get(id=pk)
    serializer = StoreSerializer(store, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def storeUpdate(request, pk):
    name = 'store-update'
    permission_classes = [IsAuthenticated]
    store = Store.objects.get(id=pk)
    serializer = StoreSerializer(instance=store, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE','GET'])
def storeDelete(request, pk):
    name = 'store-delete'
    permission_classes = [IsAuthenticated]
    store = Store.objects.get(id=pk)
    store.delete()
    return Response('Item successfully deleted')

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'vendors': reverse(VendorsList.name, request=request),
            'category': reverse(CategoryView.name, request=request),
            'estate': reverse(EstateView.name, request=request),
            'stores':reverse(StoresList.name, request=request),
            
        })
