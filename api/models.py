import uuid
from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


def recipe_image_file_path(instance, filename: str, path='uploads/recipe/'):
    """Generate file path for new recipe image"""
    extension = filename.split('.')[-1]
    uuidname = f'{uuid.uuid4()}.{extension}'

    return str(Path(path).joinpath(uuidname))


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        """Creates and save a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model support using email instead of username"""

    USERNAME_FIELD = 'email'

    email = models.EmailField('Email', max_length=254, unique=True, db_index=True)
    name = models.CharField('Name', max_length=255, blank=True)
    is_active = models.BooleanField('Is active', default=True)
    is_staff = models.BooleanField('Is staff', default=False)

    objects = UserManager()


class Tag(models.Model):
    """"Tag to be used for recipe"""
    name = models.CharField('Tag name', max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='tags',
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """"Ingredient to be used for recipe"""
    name = models.CharField('Ingredient name', max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='ingredients',
    )

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """"User recipe object"""
    title = models.CharField('Title', max_length=255, db_index=True)
    time_minutes = models.PositiveIntegerField('Minutes')
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)
    link = models.URLField('Link', max_length=255, blank=True)
    description = models.TextField('Recipe Description', blank=True)
    image = models.ImageField(
        'Image',
        upload_to=recipe_image_file_path,
        blank=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='User',
        related_name='recipes',
        on_delete=models.CASCADE,
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        verbose_name='Ingredients',
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Tags',
        related_name='recipes',
    )

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title
