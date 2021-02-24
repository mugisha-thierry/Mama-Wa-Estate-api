from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('', views.AuthViewSet,  basename='auth')
urlpatterns = router.urls

urlpatterns = [
    path('profile/', views.ProfileSerializer.as_view(),name='profile'), 
      
]


