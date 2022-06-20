from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
import datetime
# Create your views here.
from django.urls import reverse

from todo_main.models import Todo

def index(request):
    datas = Todo.objects.filter(Q(finished=None) & Q(user=request.user.pk)).order_by('deadline')
    todos = [{
        'pk' : int(data.pk),
        'todo': data.todo,
        'deadline': str(data.deadline.strftime("%Y-%m-%d"))+" "+str(data.deadline.time())[0:5]
    } for data in datas]
    return render(request, 'index.html', {'todos': todos})

def finished_list(request):
    datas = Todo.objects.filter(~Q(finished = None) & Q(user=request.user.pk)).order_by('finished')
    todos = [{
        'todo': data.todo,
        'finished': str(data.finished.strftime("%Y-%m-%d"))+" "+str(data.finished.time())[0:5],
        'deadline': str(data.deadline.strftime("%Y-%m-%d"))+" "+str(data.deadline.time())[0:5]
    } for data in datas]
    return render(request, 'finished_list.html',{"todos":todos})
def create_todo(request):
    todo = request.POST["todo"]
    deadline = request.POST["deadline"]
    new_todo = Todo(todo=todo,deadline=deadline,user=request.user)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def finish_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    Todo.objects.filter(pk=pk).update(finished=datetime.datetime.now())
    print(todo)
    return HttpResponseRedirect(reverse('index'))

def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
