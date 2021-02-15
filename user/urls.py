from .views import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('user/', UserAPI.as_view(), name='user'),

]