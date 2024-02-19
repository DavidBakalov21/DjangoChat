from django.shortcuts import render

def RenderMain(request):
    return render(request, 'main.html')
def render_info(request):
    return render(request, 'info.html')
    