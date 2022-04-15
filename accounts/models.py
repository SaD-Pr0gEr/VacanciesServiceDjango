from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Модель кастомного пользователя"""

    email = models.EmailField(
        "email пользователя",
        max_length=260,
        unique=True
    )
    city = models.ForeignKey(
        'main_app.Cities',
        related_name='city_users',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Ваш город'
    )
    language = models.ForeignKey(
        'main_app.ProgramLanguage',
        related_name='lang_users',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Ваш язык программирования'
    )
    subscribed = models.BooleanField("Подписка на рассылку", default=False)
    is_active = models.BooleanField("Активный аккаунт", default=False)
    is_superuser = models.BooleanField("Статус суперпользователя", default=False)
    is_staff = models.BooleanField("Статус персонала", default=False)
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return f'{self.email}'
    
    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Список пользателей'
