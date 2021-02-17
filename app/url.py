from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from .views import VendorsList, StoresList

from . import views

urlpatterns=[
    url(r'^api/vendors/$', views.VendorsList.as_view()),
    url(r'^api/stores/$', views.StoresList.as_view())
]