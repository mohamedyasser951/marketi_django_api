from django.urls import path
from .views import CheckoutView, AddressListCreateView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('addresses/', AddressListCreateView.as_view(), name='address_list_create'),
]
