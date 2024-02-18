from django.shortcuts import render
from log_reg.helpers import mongoConnection
from main.helpers import displayAll
client=mongoConnection.get_mongo_collection()
def my_websocket(request,User_email,friend_email):
    return render(request, 'websocket.html',{'user':User_email, 'friend':friend_email})

def render_list(request,user):
    return displayAll.display_all(request,client,user)

