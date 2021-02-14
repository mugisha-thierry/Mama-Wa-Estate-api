from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns=[
    path('api/estate/', views.estate.as_view()),
    path('api/category/', views.category.as_view())
]
