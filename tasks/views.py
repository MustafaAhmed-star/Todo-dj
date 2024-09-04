from django.shortcuts import render, HttpResponse
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