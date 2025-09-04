from rest_framework import serializers
from .models import Product,Category
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "slug", "image","description", "price"]

class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name", "image", "products"]
