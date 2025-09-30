from django.db import models


class Genres(models.Model):
    genre_name = models.CharField(
        "Genre",
        max_length=128,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
