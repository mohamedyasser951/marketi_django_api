from rest_framework import serializers
from .models import Favorite
from products.models import Product
from products.serializers import ProductSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)
    
    class Meta:
        model = Favorite
        fields = ('id', 'product', 'product_id', 'created_at')
