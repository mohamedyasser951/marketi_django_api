from django.urls import path
from .views import CartItemListCreateView, CartItemRetrieveUpdateDestroyView

urlpatterns = [
    path('', CartItemListCreateView.as_view(), name='cart_list_create'),
    path('<int:id>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cart_item_detail'),
]
