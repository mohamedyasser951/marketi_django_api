from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .models import Product, ProductRating
from .serializers import ProductSerializer, ProductRatingSerializer


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)

class ProductByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category__id=category_id)

class AddProductRatingView(generics.CreateAPIView):
    serializer_class = ProductRatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Provide a dummy queryset to prevent schema generation error."""
        return ProductRating.objects.all()  # Or return an empty queryset if you prefer

    @swagger_auto_schema(auto_schema=None)  # To hide GET method from Swagger
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

