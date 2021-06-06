from django.contrib import admin
from todo_app.todo.models import Todo, Person, Category, Priority


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "priority", "responsible_person", "state", ]
    list_filter = ["title", "category", "responsible_person", "priority", ]
    sortable_by = ["title", "category", "priority", "responsible_person", "state", ]


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Priority)