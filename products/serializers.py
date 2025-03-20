from rest_framework import serializers
from .models import Product, ProductRating, ProductGallery

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    average_rating = serializers.FloatField(read_only=True)
    primary_image_url = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()  # Plain list of URLs

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'discount_price',
            'category', 'average_rating', 'primary_image_url', 'gallery'
        )

    def get_primary_image_url(self, obj):
        request = self.context.get('request')
        if obj.primary_image:
            return request.build_absolute_uri(obj.primary_image.url)
        return None

    def get_gallery(self, obj):
        request = self.context.get('request')
        return [
            request.build_absolute_uri(gallery.image.url)
            for gallery in obj.gallery.all()
            if gallery.image
        ]

class ProductRatingSerializer(serializers.ModelSerializer):
    # User and product are set in the view
    class Meta:
        model = ProductRating
        fields = ('id', 'rating', 'comment', 'created_at')
        read_only_fields = ('id', 'created_at')
