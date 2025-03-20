from django.contrib.auth.models import AbstractUser
from django.db import models
# Import your custom manager
from .manger import CustomUserManager  # Adjust the import path as needed

class CustomUser(AbstractUser):
    username = None  # Remove the username field
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(
        upload_to='profile_images/', 
        null=True, 
        blank=True, 
        default='profile_images/default_profile.png'
    )

    USERNAME_FIELD = "email"  # Use email for authentication
    REQUIRED_FIELDS = ["name"]  # Required when creating a superuser

    # Use the custom user manager
    objects = CustomUserManager()

    def __str__(self):
        return self.email
