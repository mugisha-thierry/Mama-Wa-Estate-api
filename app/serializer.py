from rest_framework import serializers
from .models import Estate, Category, ProductMerch,Vendor



class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        




class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMerch
        fields = ('id','name', 'description', 'price','title')
        

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


        