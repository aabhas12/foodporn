from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class recipe(models.Model):
    user=models.ForeignKey(User)
    title=models.CharField(max_length=250)
    time=models.FloatField()
    Servings=models.IntegerField()
    viewcount=models.IntegerField(null=True)
    likes=models.IntegerField(null=True)
    dislikes=models.IntegerField(null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

class ingredients(models.Model):
    user=models.ForeignKey(User)
    recipe=models.ForeignKey(recipe)
    ingredient=models.CharField(max_length=75)
    quantity=models.FloatField()


class instructions(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(recipe)
    step = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()

class instructionimage(models.Model):
    instruction = models.ForeignKey(instructions)
    image = models.URLField(null=True)

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







