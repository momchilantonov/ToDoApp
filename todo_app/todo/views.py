from django.shortcuts import redirect, render
from datetime import datetime
from todo_app.todo.models.todo import Todo
from todo_app.todo.models.person import Person
from todo_app.todo.models.priority import Priority
from todo_app.todo.models.category import Category


# Home page
# Show all todos with state "NOT DONE" and due_date=today"
def index(req):
    now = datetime.now()
    todos = Todo.objects.filter(state=False, due_date=now)
    context = {
        "todos": todos,
    }

    return render(req, "index.html", context)


# All todos page
# Show all todos
def all_todos(req):
    todos = Todo.objects.all().order_by("due_date")
    context = {
        "todos": todos
    }

    return render(req, "all_todos.html", context)


#All "NOT DONE" todos page
# Show all todos with state "NOT DONE"
def not_done_todos(req):
    todos = Todo.objects.all().filter(state=False)
    context = {
        "todos": todos
    }

    return render(req, "not_done_todos.html", context)


# All "DONE" todos page
# Show all todos with state "DONE"
def done_todos(req):
    todos = Todo.objects.all().filter(state=True)
    context = {
        "todos": todos
    }

    return render(req, "done_todos.html", context)


# Create new todo page
def create_page(req):
    context = {
        "todos": Todo.objects.all(),
        "categories": Category.objects.all(),
        "priorities": Priority.objects.all(),
        "responsible_persons": Person.objects.all(),
    }

    return render(req, "create_todo.html", context)


# Create new todo
def create_todo(req):
    req_title = req.POST["title"]
    req_description = req.POST["description"]
    req_due_date = req.POST["due_date"]
    req_category = req.POST["category"]
    req_priority = req.POST["priority"]
    req_responsible_person = req.POST["responsible_person"]

    category = Category.objects.filter(name=req_category).first()
    priority = Priority.objects.filter(name=req_priority).first()
    responsible_person = Person.objects.filter(name=req_responsible_person).first()

    if not category:
        category = Category(name=req_category)
        category.save()

    if not priority:
        priority = Priority(name=req_priority)
        priority.save()

    if not responsible_person:
        responsible_person = Person(name=req_responsible_person)
        responsible_person.save()

    todo = Todo(
        title=req_title,
        description=req_description,
        due_date=req_due_date,
        category=category,
        priority=priority,
        responsible_person=responsible_person
    )
    todo.save()

    return redirect("/")


# Delete todo page
def delete_page(req, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        "todo": todo
    }

    return render(req, "delete_todo.html", context)


# Delete todo
def delete_todo(req, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect("/")


# Edit todo page
def edit_page(req, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        "todo": todo
    }

    return render(req, "edit_todo.html", context)


# Edit todo
def edid_todo(req):
    pass


# Change todo page
def change_page(req):
    pass

# Change the state of a todo
def change_state(req, pk):
    todo = Todo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()

    return redirect("/")
