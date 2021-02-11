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



