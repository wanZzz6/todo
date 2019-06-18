from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def edit(request):
    return render(request, 'edit.html')


def about(request):
    return render(request, 'about.html')