from django.http import HttpResponse
from django.shortcuts import render
from log_reg.helpers import mongoConnection, AddUser, FindUser
from django.views.decorators.csrf import csrf_exempt
client=mongoConnection.get_mongo_collection()
# Create your views here.
def render_sign_up(request):
    return render(request,'sign_up.html')

def render_sign_in(request):
    return render(request,'sign_in.html')

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        selected_role = request.POST.get('role')
        password=request.POST.get('password')
        return AddUser.add_user(request,[first_name,last_name,email,selected_role,password],client)
    else:
        return HttpResponse("Please don't access this endpoint manually")
    
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password=request.POST.get('password')
        return FindUser.login_user(request,[email,password],client)
    else:
        return HttpResponse("Please don't access this endpoint manually")
