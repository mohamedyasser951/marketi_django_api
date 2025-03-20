from django.db import models
from django.conf import settings
from categories.models import Category  # Ensure categories app is installed

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    primary_image = models.ImageField(
        upload_to='products/primary/', null=True, blank=True
    )

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            from django.db.models import Avg
            return ratings.aggregate(Avg('rating'))['rating__avg'] or 0
        return 0

class ProductGallery(models.Model):
    """
    This model stores additional images for a product.
    """
    product = models.ForeignKey(Product, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"Gallery image for {self.product.name}"

class ProductRating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_ratings', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # e.g., 1 to 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')  # one rating per user per product

    def __str__(self):
        return f"{self.user.email} - {self.product.name} ({self.rating})"
    

