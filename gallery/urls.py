from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageGalleryViewSet

router = DefaultRouter()
router.register(r'gallery', ImageGalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
