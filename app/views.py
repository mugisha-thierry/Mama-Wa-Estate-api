from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializer import EstateSerializer
from .forms import StoreForm


from .serializer import EstateSerializer,CategorySerializer,VendorSerializer
from rest_framework import mixins, viewsets , generics, status


from rest_framework import generics
from django.contrib.auth.models import User
from .models import Category, Estate, Cart, Product,Order,Vendor,CartProduct
from .serializer import EstateSerializer,CategorySerializer,CartSerializer,ProductSerializer, OrderSerializer,CartProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.forms.models import model_to_dict
from .forms import *
from django.db.models import Q


from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer


class ListCategory(generics.ListCreateAPIView):
    name = "category"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    name = "category"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListEstate(generics.ListCreateAPIView):
    name = "estate"
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

class DetailEstate(generics.RetrieveUpdateDestroyAPIView):
    name = "estate"
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

class ListCartProduct(generics.ListCreateAPIView):
    name = "cartProduct"
    queryset =CartProduct.objects.all()
    serializer_class = CartProductSerializer

class DetailCartProduct(generics.RetrieveUpdateDestroyAPIView):
    name = "cartProduct"
    queryset =CartProduct.objects.all()
    serializer_class = CartProductSerializer

class ListCart(generics.ListCreateAPIView):
    name = "cart"
    queryset =Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    name = "cart"
    queryset = Cart.objects.all()
    serializer_class = CartSerializer    

class ListProduct(generics.ListCreateAPIView):
    name = "product"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    name = "product"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    


class ListOrder(generics.ListCreateAPIView):
    name = "order"
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    
    


class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    name = "order"
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    





class AddToCartView(APIView):
    name = "add-to-cart"
    
    def post(self, request, *args, **kwargs):    
        
   
        
        # get product id from requested url
        product_id = self.kwargs['pro_id']
        # get product
        product_obj = Product.objects.get(id=product_id)

        # check if cart exists
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(
                product=product_obj)

            # item already exists in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.selling_price
                cartproduct.save()
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
                
            # new item is added in cart
            else:
                cartproduct = CartProduct.objects.create(
                    cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
                cart_obj.total += product_obj.selling_price
                cart_obj.save()

        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
            cart_obj.total += product_obj.selling_price
            cart_obj.save()
            
        
        return Response({'Added  Successfully'},status=HTTP_200_OK)
    

class PostViewSet(viewsets.ModelViewSet):
    name = "product"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VendorsList(APIView):
    name = "vendors"
    def get(self, request, format=None):
        permission_classes = [IsAuthenticated]
        all_vendors = Vendor.objects.all()
        serializers = VendorSerializer(all_vendors, many=True)
        return Response(serializers.data)

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'vendors': reverse(VendorsList.name, request=request),
            'category_list': reverse(ListCategory.name, request=request),
            'category_detail': reverse(DetailCategory.name, request=request),
            'estate_list': reverse(ListEstate.name, request=request),
            'estate_detail': reverse(DetailEstate.name, request=request),
            'cart_list': reverse(ListCart.name, request=request),
            'cart_detail': reverse(DetailCart.name, request=request),
            'product_list': reverse(ListProduct.name, request=request),
            'product_detail': reverse(DetailProduct.name, request=request),
            'checkout_list': reverse(ListOrder.name, request=request),
            'checkout_detail': reverse(DetailOrder.name, request=request),
            # 'cartproduct_list': reverse(ListCartProduct.name, request=request),
            # 'cartproduct_detail': reverse(DetailCartProduct.name, request=request),
            # 'add-to-cart': reverse(AddToCartView.name, request=request),
           
        })
        
class StoresList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        all_stores = Store.objects.all()
        serializers = StoreSerializer(all_stores, many=True)
        return Response(serializers.data)
