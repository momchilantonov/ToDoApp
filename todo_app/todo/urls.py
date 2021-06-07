from django.urls import path
from todo_app.todo.views import change_state, index, create_todo


urlpatterns = [
    path("", index),
    path("add/", create_todo),
    path("change-state/<int:pk>", change_state)
]