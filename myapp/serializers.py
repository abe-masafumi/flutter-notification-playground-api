from rest_framework import serializers
from .models import MaleUser, FemaleUser, ProfileImage, Hobby, ApiLog, CustomUser

# カスタムユーザー
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'firebase_uid', 'role']

# 男性

class MaleUserSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = MaleUser
        fields = ['user', 'username', 'birthday', 'address', 'introduction']
        read_only_fields = ['user', 'username', 'birthday', 'address']

# 
# 新規登録
# 
class MaleUserCreateSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = MaleUser
        fields = ['user', 'username', 'birthday', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        custom_user = CustomUser.objects.create(**user_data)
        male_user = MaleUser.objects.create(user=custom_user, **validated_data)
        return male_user

# 
# ユーザー編集
# 
class MaleUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleUser
        fields = ['introduction']

# 女性
class FemaleUserSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = FemaleUser
        fields = '__all__'

# プロフィール画像
class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = '__all__'

# 趣味
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = '__all__'

# ログ
class ApiLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiLog
        fields = '__all__'
