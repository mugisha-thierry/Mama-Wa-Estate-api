from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Estate
from .serializer import EstateSerializer

#........
class Estate(APIView):
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



