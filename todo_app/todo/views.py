from django.shortcuts import redirect, render
from todo_app.todo.models.todo import Todo
from todo_app.todo.models.person import Person


def todo(req):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(req, "todo.html", context=context)


def create_todo(req):
    req_title = req.POST["title"]
    req_description = req.POST["description"]
    req_responsible_person = req.POST["responsible_person"]
    responsible_person = Person.objects.filter(name=req_responsible_person).first()

    if not responsible_person:
        responsible_person = Person(name=req_responsible_person)
        responsible_person.save()

    todo = Todo(
        title=req_title,
        description=req_description,
        responsible_person=responsible_person
    )
    todo.save()

    return redirect("/")


def change_state(req, pk):
    todo = Todo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()

    return redirect("/")
