from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializer import EstateSerializer
from .forms import StoreForm
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework import mixins, viewsets , generics
from .models import ProductMerch, Estate, Vendor, Store, Category

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import EstateSerializer,CategorySerializer,MerchSerializer,VendorSerializer
from rest_framework import mixins, viewsets , generics, status


from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView


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
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        
        all_vendors = Vendor.objects.all()
        serializers = VendorSerializer(all_vendors, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        
        serializers = VendorSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

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
        
