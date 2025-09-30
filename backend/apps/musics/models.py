from django.db import models

from apps.users.models import User
from apps.genres.models import Genres

class Musics(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    genres = models.ForeignKey(
        Genres,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    music_name = models.CharField(
        "Music Name",
        max_length=128,
    )
    # TODO: Create a custom storage to protect musics from other users
    music_file = models.FileField(
        "Music File",
    )
