from rest_framework import viewsets, routers
from photo.models import User, Photo
from photo.serializers import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

router = routers.DefaultRouter()
router.register(r'photo', PhotoViewSet)
