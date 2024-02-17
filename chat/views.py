from django.http import HttpResponse
from django.shortcuts import render

def RenderMain(request):
    return render(request, 'main.html')