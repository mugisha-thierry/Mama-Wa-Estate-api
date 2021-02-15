from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from .views import VendorsList
from rest_framework.routers import SimpleRouter
from .views import PostViewSet

from . import views


from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns=[
    # url(r'^api/estate/$', views.Estate.as_view()),
    path('api/estate/', views.estate.as_view()),
    url(r'^api/vendors/$', views.VendorsList.as_view()),
    path('api/category/', views.category.as_view()),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

router = SimpleRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls

