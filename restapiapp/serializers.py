from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        #because we want all the field in our product model to serialize
        fields='__all__'
