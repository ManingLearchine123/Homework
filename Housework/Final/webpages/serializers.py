from rest_framework import serializers
from .models import Game, Review, User

class Game(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
class GameSerializer(Game):
    class Meta:
        exclude = ['description']
class DetailSerializer(Game):
    class Meta:
        exclude = ['shortdescription']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'