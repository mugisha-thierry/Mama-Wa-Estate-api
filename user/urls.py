from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=True)
router.register('', views.AuthViewSet,  basename='auth')

urlpatterns = [
    path('profile/', views.ProfileSerializer.as_view(),name='profile'), 
    path('', include(router.urls)),  
]


