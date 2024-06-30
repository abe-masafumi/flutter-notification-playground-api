from rest_framework import serializers
from .models import MaleUser, FemaleUser, ProfileImage, Hobby, ApiLog, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'firebase_uid', 'role']

class MaleUserSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = MaleUser
        fields = ['id', 'username', 'birthday', 'address',]
        read_only_fields = ['id', 'username', 'birthday', 'address']

class FemaleUserSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = FemaleUser
        fields = '__all__'

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = '__all__'

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = '__all__'

class ApiLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiLog
        fields = '__all__'
