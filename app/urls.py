from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, StoreForm

from . import views

urlpatterns=[
    url(r'^api/vendors/$', views.VendorsList.as_view()),
    url(r'^api/stores/$', views.StoresList.as_view()),
    
]

router = SimpleRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

