from django.db import models


class Priority(models.Model):
    LOW = "Low"
    NORMAL = "Normal"
    HIGH = "High"
    ALL_PRIORITIES = (
        (LOW, "Low"),
        (NORMAL, "Normal"),
        (HIGH, "High")
    )
    name = models.CharField(
        max_length=20,
        null=True,
        choices=ALL_PRIORITIES
    )

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural = "priorities"