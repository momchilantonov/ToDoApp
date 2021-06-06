from django.db import models


class Category(models.Model):
    HOME = "Home"
    WORK = "Work"
    SCHOOL = "School"
    SHOPPING = "Shopping"
    TRAINING = "Training"
    OTHER = "Other"
    ALL_CATEGORIES = (
        (HOME, "Home"),
        (WORK, "Work"),
        (SCHOOL, "School"),
        (SHOPPING, "Shopping"),
        (TRAINING, "Training"),
        (OTHER, "Other")
    )
    name = models.CharField(
        max_length=10,
        null=True,
        choices=ALL_CATEGORIES
    )

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural = "categories"