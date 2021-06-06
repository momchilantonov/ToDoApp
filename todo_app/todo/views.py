from django.shortcuts import render
from todo_app.todo.models import Todo

# Create your views here.
def index(req):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(req, "index.html", context=context)