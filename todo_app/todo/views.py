from todo_app.todo.forms.create_todo_form import CreateTodoForm
from django.shortcuts import redirect, render
from django.utils.timezone import make_aware
from datetime import datetime
from todo_app.todo.models.todo import Todo


# return form from GET request
def show_todo_form(req, form, temp):
    context = {
        'form': form,
    }
    return render(req, temp, context)


# Save new created todo with POST request
def save_new_todo(req, form, red, temp):
    if form.is_valid():
        form.save()
        return redirect(red)
    # If its not valid, return old form
    return show_todo_form(req, form, temp)


# Config the time for Django
naive_datetime = datetime.today()
current_time = make_aware(naive_datetime)
naive_datetime = naive_datetime.replace(hour=23, minute=59, second=59)
end_time = make_aware(naive_datetime)


# Show all todos with due_date=today"
def index(req):
    todos = Todo.objects.filter(due_date__gte=current_time, due_date__lte=end_time)
    temp = "index.html"
    context = {
        "todos": todos,
    }
    return render(req, temp, context)


# Create new todo form
def create_todo(req):
    if req.method == 'GET':
        form = CreateTodoForm()
        temp = 'create_todo.html'
        return show_todo_form(req, form, temp)
    form = CreateTodoForm(req.POST)
    red = "index"
    temp = "index.html"
    return save_new_todo(req, form, red, temp)

