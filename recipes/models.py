from datetime import datetime

from django.db import models

# Create your models here.
from accounts.models import UserProfile
from cloudinary import models as cloudinary_models

class Recipes(models.Model):
    title = models.CharField(max_length=30)
    image = cloudinary_models.CloudinaryField("image")
    description = models.TextField()
    ingredients = models.CharField (max_length= 250)
    time = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self): # for Django admin
        return f'{self.id}; {self.title}; {self.user}'


class Comment(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)