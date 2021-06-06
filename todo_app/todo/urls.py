from django.urls import path
from todo_app.todo.views import change_state, todo, create_todo


urlpatterns = [
    path("", todo),
    path("add/", create_todo),
    path("change-state/<int:pk>", change_state)
]