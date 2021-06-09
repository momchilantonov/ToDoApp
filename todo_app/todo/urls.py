from django.urls import path
from todo_app.todo.views import all_todos, change_state, done_todos, index, create_todo, not_done_todos


urlpatterns = [
    path("", index),
    path("all/", all_todos),
    path("done/", done_todos),
    path("not-done/", not_done_todos),
    path("change-state/<int:pk>", change_state)
]