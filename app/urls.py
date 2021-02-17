from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


# from knox import views as knox_views
# from .views import LoginAPI

router = SimpleRouter()
router.register('products', views.PostViewSet, basename='posts')

urlpatterns=[
    # url(r'^api/estate/$', views.Estate.as_view()),
    
    path('estate/', views.Estate.as_view(), name='estate'),
    path('vendors/', views.VendorsList.as_view(), name='vendors'),
    path('category/', views.Category.as_view(), name='category'),
    path('', include(router.urls)),
    # path('login/', views.LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]