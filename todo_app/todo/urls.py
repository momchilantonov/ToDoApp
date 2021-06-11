from django.urls import path
from todo_app.todo.views import all_todos, change_state, create_todo, done_todos, todays_todos, create_page, not_done_todos, login


urlpatterns = [
    path("", login, name="login"),
    path("today/", todays_todos, name="today tasks"),
    path("all/", all_todos, name="all tasks"),
    path("done/", done_todos, name="done tasks"),
    path("not-done/", not_done_todos, name="not done tasks"),
    path("create-page/", create_page, name="create page"),
    path("create-todo", create_todo, name="create todo"),
    path("change-state/<int:pk>", change_state, name="change state")
]