from rest_framework import serializers
from ..models import ProfileImage

# プロフィール画像
class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = '__all__'