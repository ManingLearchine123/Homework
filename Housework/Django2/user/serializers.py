from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
		extra_kwargs = {'password': {'write_only: True'}}
		#password hiding from API
	def create(s, v):
		u = User.objects.create_user(**v)
		return u