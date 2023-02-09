from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('tasksp/', views.tasksp, name = 'tasks'),
    path('tasksapp/', views.about, name = 'tasksapp'),
    path('tasksapp/', views.about, name = 'tasksapp'),
    path('taskpost/<int:slug>', views.taskpost, name = 'taskpost'),
    path('delete/<int:slug>', views.delete_todo, name = 'deletetodo'),
]