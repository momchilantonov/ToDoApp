from django.contrib import admin
from todo_app.todo.models import Todo, Person, Category, Priority

# Option 1 to make admin register (with property)
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "priority", "due_date", "responsible_person", "state", ]
    list_filter = ["title", "category", "responsible_person", "priority","due_date",]
    sortable_by = ["title", "category", "priority", "due_date", "responsible_person", "state", ]

    # Restrict Edit, Add, Delate ....
    # def has_change_permission(self, request, obj=None):
    #     return False


# Option 2 to make admin register (like normal register)
# admin.site.register(Todo, TodoAdmin)

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Priority)