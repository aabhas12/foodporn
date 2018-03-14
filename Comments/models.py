import django
from django.db import models

# Create your models here.
from Recipe.models import Recipe
from foodporn import settings


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.CharField(max_length=160)
    likes = models.IntegerField(default=0)
    created_at = models.DateField(default=django.utils.timezone.now)
    updated_at = models.DateField(default=django.utils.timezone.now)

    def reply_comment(self):
        return self.replycomment_set.all()


class ReplyComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='reply_comment', on_delete=models.CASCADE)
    reply = models.CharField(max_length=160)
    likes = models.IntegerField(default=0)
    created_at = models.DateField(default=django.utils.timezone.now)
    updated_at = models.DateField(default=django.utils.timezone.now)


class UserCommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='reply_comment_boolean', on_delete=models.CASCADE)