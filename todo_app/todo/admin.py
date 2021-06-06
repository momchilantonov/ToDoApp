from django.contrib import admin
from todo_app.todo.models import Todo, Person, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "state", ]
    list_filter = ["title", "category"]
    sortable_by = ["title", "state", "category", ]


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)