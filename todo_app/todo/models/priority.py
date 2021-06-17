from django.db import models


class Priority(models.Model):
    LOW = 'Low'
    NORMAL = 'Normal'
    HIGH = 'High'
    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    )
    name = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        null=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "priorities"