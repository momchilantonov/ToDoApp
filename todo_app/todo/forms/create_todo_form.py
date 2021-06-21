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
                    'style': 'color: #0066ff',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3,
                    'style':'resize:none; color: #0066ff',
                }
            ),
            'state': forms.CheckboxInput(
                attrs={
                    'class': "form-check",
                    'style': 'color: #0066ff',
                }
            ),
            'due_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                    'style': 'color: #0066ff',
                }
            ),
            'responsible_person': forms.Select(
                attrs={
                    'class': 'form-select',
                    'style': 'color: #0066ff'
                },
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                    'style': 'color: #0066ff',
                }
            ),
            'priority': forms.RadioSelect(
                attrs={
                    'class': 'form-radio',
                    'style': 'color: #0066ff',
                }
            )

        }
