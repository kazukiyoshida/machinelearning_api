from rest_framework import serializers
from photo.models import User, Photo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        Model = User

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Photo

