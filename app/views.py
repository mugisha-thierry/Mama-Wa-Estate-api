from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Estate,Category
from .serializer import EstateSerializer,CategorySerializer
from rest_framework import status

#........
class estate(APIView):
    def get(self, request, format=None):
        all_estate = Estate.objects.all()
        serializers = EstateSerializer(all_estate, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers =  EstateSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)        



class category(APIView):
    def get(self, request, format=None):
        all_category = Category.objects.all()
        serializers =CategorySerializer(all_category, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers =  CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)        



