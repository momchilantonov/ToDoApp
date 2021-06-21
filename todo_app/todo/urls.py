from django.urls import path
from todo_app.todo.views import  edit_todo, index, create_todo, show_all_todos, show_done_todos, show_not_done_todos


urlpatterns = [
    path("", index, name="index"),
    path('create_todo/', create_todo, name='create_todo'),
    path('show_all/', show_all_todos,name='show_all'),
    path('show_not_done/', show_not_done_todos, name='show_not_done'),
    path('show_done/', show_done_todos, name='show_done'),
    path('edit_todo/<int:pk>/', edit_todo, name='edit_todo'),
]
