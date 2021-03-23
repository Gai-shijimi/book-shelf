from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """カスタムユーザーマネジャー"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """emailを必須にする"""
        if not email:
            raise ValueError('正しいメールアドレスを入力してください')

        """emailでUserモデルを作成"""
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('管理者権限は、スタッフ(is_staff)でなければなりません')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('管理者権限は、管理者(is_superuser)でなければなりません')
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('管理者権限は、スタッフ(is_staff)でなければなりません')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('管理者権限は、管理者(is_superuser)でなければなりません')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""
    email = models.EmailField("メールアドレス", unique=True)
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)
    date_joined = models.DateTimeField("date_joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


