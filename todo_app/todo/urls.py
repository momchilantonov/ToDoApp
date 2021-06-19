from django.urls import path
from todo_app.todo.views import index, create_todo


urlpatterns = [
    path("", index, name="index"),
    path('create_todo/', create_todo, name='create_todo'),
]
