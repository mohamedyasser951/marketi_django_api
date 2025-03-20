from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductByCategoryView,
    AddProductRatingView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:category_id>/', ProductByCategoryView.as_view(), name='product_by_category'),
    path('<int:pk>/rate/', AddProductRatingView.as_view(), name='add_product_rating'),
]
