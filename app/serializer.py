from rest_framework import serializers
from .models import Estate


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

        