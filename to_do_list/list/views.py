from django.shortcuts import render
from list.models import *


# Create your views here.


def todo(request):
    todolist = todo_list.objects.all()
    return render(request, 'todo.html', locals())


def add(request):
    todolist = todo_list.objects.all()
    if request.method == 'POST':
        thing = request.POST['Item']
        todo_list.objects.create(thing=thing)
        return render(request, 'demo.html', locals())
    else:
        return render(request, 'demo.html', locals())


def deletelist(request):
    todolist = todo_list.objects.all()
    if request.method == 'POST':
        thing = request.POST['Delete']
        todo_list.objects.get(thing=thing).delete()
        return render(request, 'demo.html', locals())
    else:
        return render(request, 'demo.html', locals())


def updatelist(request):
    todolist = todo_list.objects.all()
    if request.method == 'POST':
        thing = request.POST['update']
        thing1 = request.POST['update1']
        todo_list.objects.filter(thing=thing1).update(thing=thing)
        return render(request, 'demo.html', locals())
    else:
        return render(request, 'demo.html', locals())


def updatestate(request):
    todolist = todo_list.objects.all()
    if request.method == 'POST':
        state1 = int(request.POST['check_input'])
        thing4 = request.POST['check_thing']
        todo_list.objects.filter(thing=thing4).update(state=state1)
        return render(request, 'demo.html', locals())
    else:
        return render(request, 'demo.html', locals())
