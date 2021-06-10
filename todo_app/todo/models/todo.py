from django.db import models
from django.utils import timezone 
from todo_app.todo.models.person import Person
from todo_app.todo.models.category import Category
from todo_app.todo.models.priority import Priority


class Todo(models.Model):
    title = models.CharField(
        max_length=20,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    state = models.BooleanField(
        default=False,
    )
    due_date = models.DateTimeField(
        default=timezone.now
    )
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
    
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f"{self.id}: {self.title}"
