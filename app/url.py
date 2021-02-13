from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from .views import VendorsList

from . import views

urlpatterns=[
    url(r'^api/vendors/$', views.VendorsList.as_view())
]