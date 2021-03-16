from django.shortcuts import render

# Create your views here.

def app1(request):
    return render(request, 'app1.html', {})

def about(request):
    return render(request, 'about.html', {})
