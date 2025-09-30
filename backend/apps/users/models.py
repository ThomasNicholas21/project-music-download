from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator

from apps.users.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        "Username",
        max_length=160,
        unique=True,
    )
    password = models.CharField(
        "Password",
        max_length=128,
        validators=[MinLengthValidator(6)],
    )
    name = models.CharField(
        "Name",
        max_length=128,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        "Active",
        default=False,
    )
    is_staff = models.BooleanField(
        "Staff",
        default=False,
    )
    created_at = models.DateTimeField(
        "Created At",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        "Updated At",
        auto_now=True
    )
    last_login = models.DateTimeField(
        "Last Login",
        null=True,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD  = "username"
    EMAIL_FIELD = "email"
    PASSWORD_FIELD = "password"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
