from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
import datetime



class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=250)
    time = models.FloatField()
    servings = models.IntegerField()
    icon = models.ImageField(null=True)
    viewcount = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(null=True)

    def get_comments(self):
        return self.comment_set.all()

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes_ingredients',on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=75)
    quantity = models.FloatField()


class Instructions(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes_instructions',on_delete=models.CASCADE)
    step = models.CharField(max_length=300)
    image = models.ImageField(null=True)
    created_at = models.DateField(default=datetime.datetime.now())
    updated_at = models.DateField(null=True)


class RecipeVideo(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_video')
    video = models.CharField(max_length=250, null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    recipe = models.ForeignKey(Recipe)
    comment = models.CharField(max_length=160)
    likes = models.IntegerField(default=0)
    created_at = models.DateField(default=datetime.datetime.now())
    updated_at = models.DateField(default=datetime.datetime.now())

    def reply_comment(self):
        return self.replycomment_set.all()


class ReplyComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.ForeignKey(Comment, related_name='reply_comment')
    reply = models.CharField(max_length=160)
    likes = models.IntegerField(default=0)
    created_at = models.DateField(default=datetime.datetime.now())
    updated_at = models.DateField(default=datetime.datetime.now())


class UserCommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.ForeignKey(Comment, related_name='reply_comment_boolean')

