from django.shortcuts import render,redirect
from django.views.generic import FormView,View,TemplateView,CreateView,ListView,DetailView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

from app.form import TodosForm,TodoChangeForm
from app.models import Todos,Task



class IndexView(TemplateView):
    template_name="home.html"

class TodoCreateView(CreateView):
    model=Todos
    form_class=TodosForm
    template_name="todo-create.html"
    success_url=reverse_lazy("todo_list")

class TodoListView(ListView):
    model=Todos
    template_name="todo-list.html"
    context_object_name="todos"

class TodoDetailView(DetailView):
    model=Todos
    template_name="todo-detail.html"
    context_object_name="todo"


class TodoEditView(UpdateView):
    model=Todos
    form_class=TodoChangeForm
    template_name="todo-update.html"
    success_url=reverse_lazy('todo_list')

    def form_valid(self, form):
        messages.success(self.request,"Changed")
        return super().form_valid(form)

class TodoDeleteView(View): 
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.get(id=id).delete()
        messages.success(request,"todo deleted successfully")
        return redirect('todo_list')
    
class WeatherIndexView(TemplateView):
    template_name="weather.html"

