from django.urls import path
from todo_app.todo import views


urlpatterns = [
    path("", views.index)
]