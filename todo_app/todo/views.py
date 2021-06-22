from todo_app.todo.forms.create_todo_form import CreateTodoForm
from django.shortcuts import redirect, render
from django.utils.timezone import make_aware
from datetime import datetime
from todo_app.todo.models.todo import Todo


# Get todo id
def get_id(pk):
    return Todo.objects.get(pk=pk)


# return form from GET request
def show_todo_form(req, form, temp):
    context = {
        'form': form,
    }
    return render(req, temp, context)


# Save new created todo with POST request
def save_todo(req, form, temp):
    if form.is_valid():
        form.save()
        return redirect('index')
    # If its not valid, return old form
    return show_todo_form(req, form, temp)


# Config the time for Django
naive_datetime = datetime.today()
current_time = make_aware(naive_datetime)
naive_datetime = naive_datetime.replace(hour=23, minute=59, second=59)
end_time = make_aware(naive_datetime)


# Home page. Show all todos with due_date=today"
def index(req):
    todos = Todo.objects.filter(
        due_date__gte=current_time, due_date__lte=end_time)
    context = {
        "todos": todos,
    }
    return render(req, "index.html", context)


# Show all todos
def show_all_todos(req):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(req, 'show_all.html', context)


# Show all not done todos
def show_not_done_todos(req):
    todos = Todo.objects.filter(state=False)
    context = {
        'todos': todos
    }
    return render(req, 'show_not_done.html', context)


# Show all done todos
def show_done_todos(req):
    todos = Todo.objects.filter(state=True)
    context = {
        'todos': todos
    }
    return render(req, 'show_done.html', context)


# Create new todo
def create_todo(req):
    if req.method == 'GET':
        form = CreateTodoForm()
        return show_todo_form(req, form, 'create_todo.html')
    form = CreateTodoForm(req.POST)
    return save_todo(req, form, "index.html")


# Edit exist todo
def update_todo(req, pk):
    todo = get_id(pk)
    if req.method == 'GET':
        form = CreateTodoForm(initial=todo.__dict__)
        return show_todo_form(req, form, 'update_todo.html')
    form = CreateTodoForm(
        req.POST,
        instance=todo,
    )
    return save_todo(req, form, 'update_todo.html')


# Delete rxist todo with confirm popup
def delete_todo(req, pk):
    todo = get_id(pk)
    if req.method == "GET":
        form = CreateTodoForm()
        return show_todo_form(req, form, 'delete_todo.html')
    todo.delete()
    return redirect('index')
