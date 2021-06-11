from django.db import models


class User(models.Model):
    username = models.CharField(
        max_length=30,
    )
    password = models.CharField(
        max_length=20
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name_plural = "users"