from rest_framework import viewsets
from .models import ImageGallery
from .serializers import ImageGallerySerializer

class ImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = ImageGallery.objects.all().order_by('-uploaded_at')
    serializer_class = ImageGallerySerializer
