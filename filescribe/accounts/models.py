from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class FS_UserManager(BaseUserManager):
    # create normal user
    def create_user(self, email, username, password):
        if not email:
            raise ValueError(_('Email must be set'))
        if not password:
            raise ValueError(_('Password must be set'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

    # create super user
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user
        


class FS_User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = FS_UserManager()

    def __str__(self):
        return self.username + self.email

    class Meta:
        verbose_name = 'User'
