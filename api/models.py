from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        """Create and save a new user"""
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model support using email instead of username"""

    USERNAME_FIELD = 'email'

    email = models.EmailField('Email', max_length=254, unique=True, db_index=True)
    name = models.CharField('Name', max_length=255)
    is_active = models.BooleanField('Is active', default=True)
    is_staff = models.BooleanField('Is staff', default=False)

    objects = UserManager()
