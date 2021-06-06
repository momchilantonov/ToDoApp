from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=30,
        null=True,
    )

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural = "people"