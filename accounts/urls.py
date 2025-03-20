from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import RegisterView, UserProfileView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    # Login endpoint: returns both access and refresh tokens
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Refresh endpoint: returns a new access token given a valid refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # (Optional) Token verification endpoint
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Logout endpoint: blacklist the provided refresh token
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    # Endpoint to view/update the user's profile
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
