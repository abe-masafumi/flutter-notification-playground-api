from rest_framework import serializers
from ..models import MaleUser, FemaleUser, CustomUser

# 男性
class MaleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleUser
        fields = '__all__'

# 女性
class FemaleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FemaleUser
        fields = '__all__'

# カスタムユーザー
class CustomUserCreateSerializer(serializers.ModelSerializer):
    user = serializers.DictField(write_only=True, required=True)
    male_user = MaleUserSerializer(read_only=True)
    female_user = FemaleUserSerializer(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'firebase_uid', 'role', 'username', 'birthday', 'user', 'male_user', 'female_user']

    def validate(self, data):
        user_data = data.get('user', {}) 
        if data['role'] == 'MALE' and not user_data.get('address'):
            raise serializers.ValidationError({"address": "This field is required for male users."}) 
        return data

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        custom_user = CustomUser.objects.create(**validated_data)
        
        if custom_user.role == 'MALE':
            MaleUser.objects.create(user=custom_user, **user_data)
        elif custom_user.role == 'FEMALE':
            FemaleUser.objects.create(user=custom_user)
        
        return custom_user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.role == 'MALE':
            try:
                male_user = MaleUser.objects.get(user=instance)
                representation['male_user'] = {
                    'address': male_user.address,
                    'introduction': male_user.introduction,
                }
            except MaleUser.DoesNotExist:
                representation['male_user'] = None
        elif instance.role == 'FEMALE':
            try:
                female_user = FemaleUser.objects.get(user=instance)
                representation['female_user'] = {
                    'introduction': female_user.introduction,
                }
            except FemaleUser.DoesNotExist:
                representation['female_user'] = None
        return representation




