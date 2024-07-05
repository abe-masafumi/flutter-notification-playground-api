from rest_framework import serializers
from ..models import FemaleUser, CustomUser

# カスタムユーザー
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

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

# 単一ユーザー取得
class FemaleUserRetrieveSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = FemaleUser
        fields = ['user', 'introduction']
