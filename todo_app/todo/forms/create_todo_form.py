from todo_app.todo.models.todo import Todo
from django import forms




class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                }
            ),
            'state': forms.CheckboxInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'due_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                }
            ),
            'responsible_person': forms.Select(
                attrs={
                    'calss': 'forms-control',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'priority': forms.Select(
                attrs={
                    'class': 'forms-control',
                }
            )

        }
