from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('tasks/',views.taskList,name='tasks'),
]
