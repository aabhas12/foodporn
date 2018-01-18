from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Users(models.Model):
    firstname = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30,null=True)
    username = models.CharField(unique=True,max_length=30,null=True)
    avatar = models.URLField(null=True)
    social_media_id = models.CharField(null=True,max_length=30)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(null=True)

