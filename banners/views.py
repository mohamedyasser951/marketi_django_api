from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Banner
from .serializers import BannerSerializer

class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = (AllowAny,)
