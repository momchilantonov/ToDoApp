from todo_app.todo import models
from django.contrib import admin
from todo_app.todo.models import Todo

# Register your models here.
admin.site.register(models.Todo)