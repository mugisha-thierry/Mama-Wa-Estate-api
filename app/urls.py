# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls import url,include

# from . import views

# urlpatterns=[
# ]
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet

router = SimpleRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls