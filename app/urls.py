from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet

from . import views

urlpatterns=[
    url(r'^api/estate/$', views.Estate.as_view())
]

router = SimpleRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls

