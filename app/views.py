from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import EstateSerializer
from .forms import StoreForm


from rest_framework import mixins, viewsets , generics
from .models import ProductMerch, Estate, Vendor
from .serializer import MerchSerializer, VendorSerializer

# Create your views here.

@login_required(login_url='/accounts/login/')
def createStore(request):
    if request.method == 'POST':
        store_form = StoreForm(data = request.POST)
        if store_form.is_valid():
            new_store  = store_form.save()
    else:
        store_form = StoreForm()
    
    return HttpResponse('Store Creation form needs to be displayed at this point')

class Estate(APIView):
    def get(self, request, format=None):
        all_estate = Estate.objects.all()
        serializers = EstateSerializer(all_estate, many=True)
        return Response(serializers.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = ProductMerch.objects.all()
    serializer_class = MerchSerializer

class VendorsList(APIView):
    def get(self, request, format=None):
        all_vendors = Vendor.objects.all()
        serializers = VendorSerializer(all_vendors, many=True)
        return Response(serializers.data)