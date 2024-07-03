from rest_framework import serializers
from ..models import MaleUser, Hobby, CustomUser

# カスタムユーザー
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

# 趣味
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['id', 'user', 'type']

# 男性
class MaleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleUser
        fields = '__all__'

# ユーザー編集
class MaleUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleUser
        fields = ['introduction']

# 単一ユーザー取得
class MaleUserRetrieveSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    hobbies = HobbySerializer(many=True, read_only=True)

    class Meta:
        model = MaleUser
        fields = ['user', 'hobbies', 'address', 'introduction']