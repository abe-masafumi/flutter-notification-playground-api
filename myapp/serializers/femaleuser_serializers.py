from rest_framework import serializers
from ..models import FemaleUser

# 女性
class FemaleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FemaleUser
        fields = '__all__'

# ユーザー編集
class FemaleUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FemaleUser
        fields = ['introduction']
