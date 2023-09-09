from django import forms

from app.models import Todos

class TodosForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields="__all__"
        widgets={
            "todo_name":forms.TextInput(attrs={"class":"form-control border-dark text-white"}),
            "status":forms.CheckboxInput(attrs={"class":"form-check-input border-dark"})
        }

class TodoChangeForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["todo_name","status"]
        widgets={
            "todo_name":forms.TextInput(attrs={"class":"form-control"}),
            "status":forms.CheckboxInput(attrs={"class":"form-check-input"})
        }

