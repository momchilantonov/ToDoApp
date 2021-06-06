from django.urls import path
from todo_app.todo.views import index


urlpatterns = [
    path("", index)
]