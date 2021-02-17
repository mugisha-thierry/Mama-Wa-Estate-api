from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Estate,Category,ProductMerch,Vendor
from .serializer import EstateSerializer,CategorySerializer,MerchSerializer,VendorSerializer
from rest_framework import mixins, viewsets , generics, status


from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView

# Create your views here.

class Estate(APIView):
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



class Category(APIView):
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

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'vendors': reverse(VendorsList.name, request=request),
            'category': reverse(Category.name, request=request),
            'estate': reverse(Estate.name, request=request),
        })
        
# class LoginAPI(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)