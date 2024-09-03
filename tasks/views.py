from django.shortcuts import render, HttpResponse
from .models import Task


def index(requeset):

    return HttpResponse("Hello, World!")

def taskList(request):
    tasks = Task.objects.all()
    
    context = {'tasks':tasks}
    
    return render(request,'tasks.html',context)