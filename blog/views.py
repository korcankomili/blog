from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', {})

def blog(request):
    return render(request, 'blog.html', {})

