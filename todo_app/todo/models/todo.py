from django.db import models
from todo_app.todo.models.person import Person
from todo_app.todo.models.category import Category


class Todo(models.Model):
    title = models.CharField(
        max_length=20,
    )
    description = models.TextField()
    responsible_person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
    )
    state = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.id}: {self.title}"
