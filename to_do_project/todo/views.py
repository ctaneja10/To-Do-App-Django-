from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import tasks
# Create your views here.
def home(request):
    if request.method == 'POST':
        task_slug = request.POST.get('slug')
        title_main = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        s = tasks(task_slug = task_slug, title_main = title_main, sub_title = sub_title)
        s.save()
    return render(request, 'todo/home.html')

def tasksp(request):
    all_tasks = tasks.objects.all()
    return render(request, 'todo/tasks.html', {'all_tasks': all_tasks})

def taskpost(request, slug):
    all_tasks = tasks.objects.filter(task_slug = slug)[0]
    return render(request, 'todo/taskpost.html', {'all_tasks':all_tasks})

def delete_todo(request, slug):
    all_tasks = tasks.objects.filter(task_slug=slug)
    all_tasks.delete()
    return redirect('tasks')

def about(request):
    return render(request, 'todo/about.html')

