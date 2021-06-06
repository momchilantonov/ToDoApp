from django.shortcuts import render
from todo_app.todo.models.todo import Todo


def todo(req):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(req, "todo.html", context=context)