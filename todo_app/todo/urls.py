from django.urls import path
from todo_app.todo.views import todo


urlpatterns = [
    path("", todo)
]