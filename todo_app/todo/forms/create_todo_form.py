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
                    'style': 'color: #15151e;',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3,
                    'style':'resize:none; color: #15151e;',
                }
            ),
            'state': forms.CheckboxInput(
                attrs={
                    'class': "form-check",
                    'style': 'color: #15151e;',
                }
            ),
            'due_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                    'style': 'color: #15151e;',
                }
            ),
            'responsible_person': forms.Select(
                attrs={
                    'class': 'form-select',
                    'style': 'color: #15151e;'
                },
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                    'style': 'color: #15151e;;',
                }
            ),
            'priority': forms.RadioSelect(
                attrs={
                    'class': 'form-radio',
                    'style': 'color: #15151e;',
                }
            )

        }
