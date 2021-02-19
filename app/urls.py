from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ListCategory, DetailCategory, ListEstate, DetailEstate,ListCart, DetailCart,ListProduct, DetailProduct,ListOrder,DetailOrder
from . import views

router = SimpleRouter()
router.register('products', views.PostViewSet, basename='posts')

urlpatterns=[
    
    path('vendors/', views.VendorsList.as_view(), name='vendors'),
    path('', include(router.urls)),
    path('vendors/', views.VendorsList.as_view(), name='vendors'),
    path('category/', ListCategory.as_view(), name='category'),
    path('category/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    
    path('estate/', ListEstate.as_view(), name='estate'),
    path('estate/<int:pk>/', DetailEstate.as_view(), name='singlestate'),

    path('cart/', ListCart.as_view(), name='cart'),
    path('cart/<int:pk>/', DetailCart.as_view(), name='cart'),

    path('product/', ListProduct.as_view(), name='product'),
    path('product/<int:pk>/', DetailProduct.as_view(), name='product'),

    # path('add-to-cart/<int:pro_id>/', AddToCartView.as_view(), name='add-to-cart'),
    # =path('checkout/', views.CheckoutView.as_view(), name='checkout'),

    path('checkout/', ListOrder.as_view(), name='order'),
    path('checkout/<int:pk>/', DetailOrder.as_view(), name='order'),

]

