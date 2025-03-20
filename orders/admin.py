from django.contrib import admin
from .models import Address, Order, OrderItem

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'street', 'city', 'state', 'zipcode', 'country')
    search_fields = ('user__email', 'street', 'city')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'quantity', 'price')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]

admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)
