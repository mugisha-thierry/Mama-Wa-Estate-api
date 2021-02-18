from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import EstateSerializer,CategorySerializer,VendorSerializer
from rest_framework import mixins, viewsets , generics, status


from rest_framework import generics
from django.contrib.auth.models import User
from .models import Category, Estate, Cart, Product,CartProduct,Order
from .serializer import EstateSerializer,CategorySerializer,CartSerializer,ProductSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView

# Create your views here.

# class Estate(APIView):
#     name = "estate"
#     def get(self, request, format=None):
#         all_estate = Estate.objects.all()
#         serializers = EstateSerializer(all_estate, many=True)
#         return Response(serializers.data)


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListEstate(generics.ListCreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

class DetailEstate(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

class ListCart(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    


class ListOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    



class CategoryView(APIView):
    name = "category"
    def get(self, request, format=None):
        all_category = Category.objects.all()
        serializers =CategorySerializer(all_category, many=True)
        return Response(serializers.data)

class AddToCartView(APIView):
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

            return Response(status=HTTP_200_OK)

             

class CheckoutView(APIView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj = None
        
        return Response(status=HTTP_200_OK)

           

class PostViewSet(viewsets.ModelViewSet):
    name = "product"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
        
