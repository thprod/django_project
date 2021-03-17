from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def daniel(request):
    return render(request, 'daniel.html', {})

def taylor(request):
    return render(request, 'taylor.html', {})

def jesus(request):
    return render(request, 'jesus.html', {})

def about(request):
    return render(request, 'about.html', {})
