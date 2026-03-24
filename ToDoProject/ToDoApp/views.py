from django.shortcuts import render, redirect
from ToDoApp.models import ToDo
from django.contrib import messages

def AddTask(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        task = request.POST.get('task')
        if name and task:
            ToDo.objects.create(name=name, task=task)
            messages.info(request, message="Your task has been added to the list")
            return redirect('Index')
    return render(request, 'ToDoApp/index.html')

def GetTasks(request):
    tasks = ToDo.objects.all()
    return render(request, 'ToDoApp/tasks.html', {'tasks':tasks})

def cross(request, id):
    task = ToDo.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('TaskList')

def uncross(request, id):
    task = ToDo.objects.get(id=id)
    task.completed = False
    task.save()
    return redirect('TaskList')