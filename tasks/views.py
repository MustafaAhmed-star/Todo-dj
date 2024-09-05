from django.shortcuts import render, HttpResponse,redirect
from .models import Task
from .forms import TaskForm

def index(requeset):

    return HttpResponse("Hello, World!")

def taskList(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    tasks = Task.objects.all()
    
    context = {'tasks':tasks,'form':form}
    
    return render(request,'tasks.html',context)
    
    
def updateTask(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance =task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
            
    context = {'task':task,'form':form}
    
    return render(request,'update_task.html',context)
    
    
def deleteTask(request,pk):
    task = Task.objects.get(id = pk)
    if request.method =="POST":
        task.delete()
        
        return redirect('/tasks/')
    context = {'task':task}
    return render(request,'delete.html',context)