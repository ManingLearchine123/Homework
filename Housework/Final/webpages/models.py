from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

'''class SocialUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    github_id = models.CharField(max_length=100, unique=True)
    def __str__(s):
        return f'user {s.title()}'''

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(s):
        return f'user {s.title()}'

class Game(models.Model):
    title = models.CharField(max_length=100)
    shortdescription = models.CharField(max_length=50)
    description = models.TextField()
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(s):
        return s.title()

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #def __str__(s):
        #return f"Review by {s.writer.username} for {s.game.title}"