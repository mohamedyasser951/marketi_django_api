from django.contrib import admin
from .models import Product, ProductRating,ProductGallery

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'average_rating')
    search_fields = ('name', 'description')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRating)
admin.site.register(ProductGallery)
