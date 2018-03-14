import django
from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
import datetime



class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    time = models.FloatField()
    servings = models.IntegerField()
    icon = models.ImageField(null=True)
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    updated_at = models.DateTimeField(null=django.utils.timezone.now)

    def get_comments(self):
        return self.comment_set.all()


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes_ingredients', on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=75)
    quantity = models.FloatField()


class Instructions(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes_instructions', on_delete=models.CASCADE)
    step = models.CharField(max_length=300)
    image = models.ImageField(null=True)
    created_at = models.DateField(default=django.utils.timezone.now)
    updated_at = models.DateField(null=django.utils.timezone.now)


class RecipeVideo(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_video', on_delete=models.CASCADE)
    video = models.CharField(max_length=250, null=True, blank=True)



