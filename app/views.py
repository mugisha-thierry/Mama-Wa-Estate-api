from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import EstateSerializer

from rest_framework import mixins, viewsets , generics
from .models import ProductMerch, Estate
from .serializer import MerchSerializer

# Create your views here.
class Estate(APIView):
    def get(self, request, format=None):
        all_estate = Estate.objects.all()
        serializers = EstateSerializer(all_estate, many=True)
        return Response(serializers.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = ProductMerch.objects.all()
    serializer_class = MerchSerializer

