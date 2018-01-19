from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

import datetime
# Create your models here.

class Users(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, null=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    password = models.CharField(_('password'), max_length=128, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    social_media_id = models.CharField(null=True, max_length=30)
    updated_at = models.DateTimeField(null=True, blank=True)



