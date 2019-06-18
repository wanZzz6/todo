from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'todolist/home.html')


def edit(request):
    return render(request, 'todolist/edit.html')


def about(request):
    return render(request, 'todolist/about.html')