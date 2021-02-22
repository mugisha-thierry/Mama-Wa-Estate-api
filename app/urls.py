from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('products', views.PostViewSet, basename='posts')

urlpatterns=[
    path('estate/', views.EstateView.as_view(), name='estate'),
    path('vendors/', views.VendorsList.as_view(), name='vendors'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('stores/', views.StoresList.as_view(), name='stores'),
    path('store-detail/<int:pk>/', views.storeDetail, name='store-detail'),
    path('store-update/<int:pk>/', views.storeUpdate, name='store-update'),
    path('store-delete/<int:pk>/', views.storeDelete, name='store-delete'),
    path('', include(router.urls)),

]
