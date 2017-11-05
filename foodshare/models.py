from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class recipe(models.Model):
    user=models.ForeignKey(User)
    title=models.CharField(max_length=250)
    time=models.FloatField()
    Servings=models.IntegerField()
    viewcount=models.IntegerField(null=True)
    likes=models.IntegerField(null=True)
    dislikes=models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(null=True)

class ingredients(models.Model):
    recipe = models.ForeignKey(recipe,related_name='recipes_ingredients',on_delete=models.CASCADE)
    ingredient=models.CharField(max_length=75)
    quantity=models.FloatField()


class instructions(models.Model):
    recipe = models.ForeignKey(recipe,related_name='recipes_instructions',on_delete=models.CASCADE)
    step = models.CharField(max_length=300)
    image = models.ImageField(null=True)
    created_at = models.DateField(default=datetime.datetime.now())
    updated_at = models.DateField(null=True)


class recipevideo(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(recipe)
    video=models.URLField(null=True)

class comment(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(recipe)
    comment = models.CharField(max_length=160)
    likes = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

class replycomment(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(comment)
    reply = models.CharField(max_length=160)
    likes = models.IntegerField
    created_at = models.DateField()
    updated_at = models.DateField()







