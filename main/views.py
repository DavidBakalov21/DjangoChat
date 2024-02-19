from django.shortcuts import render
from django.http import HttpResponse
from log_reg.helpers import mongoConnection
from main.helpers import displayAll, displayUser, UpdateUser
client=mongoConnection.get_mongo_collection()
def my_websocket(request,User_email,friend_email):
    return render(request, 'websocket.html',{'user':User_email, 'friend':friend_email})

def render_list(request,user):
    return displayAll.display_all(request,client,user)

def render_profile(request,user):
    return displayUser.display_user(request,client,user)


def render_update(request,user):
    return render(request, 'UpadetUser.html',{'user':user})

def update_profile(request,user):
    if request.method == "POST":
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       email = request.POST.get('email')
       selected_role = request.POST.get('role')
       password=request.POST.get('password')
       first_email=request.POST.get('firstEmail')
       data={"first_name": first_name, "last_name": last_name, "email": email, "selected_role": selected_role,"password": password}
       return UpdateUser.update_user(request,data,client,first_email)
    else:
        return HttpResponse("Please don't access this endpoint manually")

