# from .views import RegisterAPI, LoginAPI, UserAPI
# from knox import views as knox_views
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('', views.AuthViewSet,  basename='auth')
router.register('profile', views.ProfileList, basename= 'profile')
urlpatterns = router.urls

urlpatterns = [
    path('profile/', views.ProfileList.as_view(), name='profile'),
    
]


