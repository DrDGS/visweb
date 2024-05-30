from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def threedmax(request):
    return render(request, 'main/threedmax.html')

def opengl(request):
    return render(request, 'main/opengl.html')

def ue(request):
    return render(request, 'main/ue.html')

def unity(request):
    return render(request, 'main/unity.html')