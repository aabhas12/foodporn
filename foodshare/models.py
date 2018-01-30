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

class UsersAssociations(models.Model):
    main_user = models.ForeignKey(Users, related_name='first_user')
    follow_user = models.ForeignKey(Users, related_name='second_user')

    def get_follow_user_count(self):
        return UsersAssociations.objects.filter(main_user=self).count()

    def get_follow_user(self):
        return UsersAssociations.objects.filter(main_user=self)

    def set_follow_user(self, myuser):
        if not UsersAssociations.objects.filter(main_user=self, follow_user=myuser).exists():
            UsersAssociations.objects.create(main_user=self, follow_user=myuser)



