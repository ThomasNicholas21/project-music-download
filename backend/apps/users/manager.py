from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.

    This manager provides methods to create users and superusers
    with email and password.
    """

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a regular user with the given username and password.

        Args:
            username (str): The username of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields for the user model.

        Returns:
            User: The created user instance.
        """

        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """
        Create and save a regular user with the given username and password.

        Args:
            username (str): The username of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields for the user model.

        Returns:
            User: The created user instance.
        """

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Create and save a superuser with the given username and password.

        Args:
            username (str): The username of the superuser.
            password (str): The password for the superuser.
            **extra_fields: Additional fields for the user model.

        Returns:
            User: The created superuser instance.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self._create_user(username, password, **extra_fields)
