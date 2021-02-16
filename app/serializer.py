from rest_framework import serializers
from rest_framework import serializers
from .models import ProductMerch
class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMerch
        fields = ('id','name', 'description', 'price','title','quantity','category','description','picture')
