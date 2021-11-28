from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'  # змінюємо дефолтну назву object_list на tasks (в task_list.html)


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'  # змінюємо дефолтну назву object на task (в task.html)
    template_name = 'base/task.html'  # - додаємо, бо змінили назву з task_detail.html на просто task.html


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

