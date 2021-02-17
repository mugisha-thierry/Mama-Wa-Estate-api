from rest_framework import serializers
from .models import Estate, Vendor, Store
from .models import ProductMerch


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMerch
        fields = ('id','name', 'description', 'price','title')

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'service')