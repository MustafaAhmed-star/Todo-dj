from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('tasks/',views.taskList,name='tasks'),
    path('tasks/<str:pk>/',views.taskDetail,name='task-detail'),
    path('tasks/<str:pk>/update/',views.updateTask,name='update-task'),
    path('tasks/<str:pk>/delete/',views.deleteTask,name='delete-task'),
]
