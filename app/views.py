from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets , generics
from .models import ProductMerch
from .serializer import MerchSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = ProductMerch.objects.all()
    serializer_class = MerchSerializer