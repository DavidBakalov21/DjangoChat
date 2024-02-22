from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from log_reg.helpers import mongoConnection
from main.helpers import displayAll, displayUser, UpdateUser, GetRoomMessages, MongoMessage, GetStudentsOnly, CheckRole, displayTeacherPage
from main.helpers import DeleteUser
client=mongoConnection.get_mongo_collection()
all_messeges=MongoMessage.get_mongo_message_collection()
def my_websocket(request,User_email,friend_email):
    message_list=GetRoomMessages.get_all_room_messages(all_messeges,User_email,friend_email)
    return render(request, 'websocket.html',{'user':User_email, 'friend':friend_email, 'messages':message_list})

def render_list(request,user):
    checkRole=CheckRole.check_role(client, user)
    if checkRole=="student":
        return displayAll.display_all(request,client,user)
    else:
        return displayTeacherPage.display_all_teacher(request,client,user)

def render_profile(request,user):
    return displayUser.display_user(request,client,user)


def render_update(request,user):
    return render(request, 'UpadetUser.html',{'user':user})

def render_delete(request,user):
    students=GetStudentsOnly.Get_Students_only(client)
    return render(request, 'DeleteList.html',{'user':user, 'items':students})

@csrf_exempt
def delete_user(request,user):
    if request.method == "DELETE":
        data = json.loads(request.body)
        email = data.get('email')
        DeleteUser.delete_user(client,email)
        students=GetStudentsOnly.Get_Students_only(client)
        return render(request, 'DeleteList.html',{'user':user, 'items':students})
    else:
        return HttpResponse("Please don't access this endpoint manually")

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

