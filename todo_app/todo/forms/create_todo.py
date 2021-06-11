from django import forms




class CreateTodoForm(forms.Form):
    title = forms.CharField(
        max_length=20,
    )
    description = forms.CharField(

    )
    # due_date = forms.DateTimeField()