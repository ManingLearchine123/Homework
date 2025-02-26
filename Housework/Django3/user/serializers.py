from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data): # {"key": "value"}
        """사용자 생성 시 비밀번호를 해싱"""
        user = User.objects.create_user(**validated_data)
        return user