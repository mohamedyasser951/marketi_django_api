from rest_framework import serializers
from .models import Address, Order, OrderItem

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('user',)

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('order', 'price',)

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)
    address_id = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(), write_only=True, source='address')
    
    class Meta:
        model = Order
        fields = ('id', 'user', 'address', 'address_id', 'total_price', 'status', 'created_at', 'order_items')
        read_only_fields = ('id', 'user', 'total_price', 'status', 'created_at', 'order_items')
