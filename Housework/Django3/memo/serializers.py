from rest_framework import serializers
from .models import Memo
#Need to add on settings
class MSerializer(serializers.ModelSerializer):
	class Meta:
		model = Memo
		fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']