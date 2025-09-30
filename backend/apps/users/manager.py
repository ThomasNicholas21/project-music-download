from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username,
            password=password,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(
            username,
            password=password,
            **extra_fields,
        )
        user.is_admin = True
        user.save(using=self._db)

        return user
