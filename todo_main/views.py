from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from todo_main.models import Todo


def index(request):
    _todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': _todos})

def create_todo(request):
    content = request.POST['todoContent']
    new_todo = Todo(title=content)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
def delete_todo(request):
    _id = request.GET['todoNum']
    todo = Todo.objects.get(id=_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
