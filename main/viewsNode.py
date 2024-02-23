import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from main.helpers import CheckRole
from log_reg.helpers import mongoConnection
from chat.settings import NODE_ENDPOINT 
client=mongoConnection.get_mongo_collection()

def redirect_GET_req_to_express(request,user):
    if CheckRole.check_role(client,user)=="teacher":
        try:
            response = requests.get(NODE_ENDPOINT,headers={"Origin":"http://127.0.0.1:8000"})
            print(response.json())
            try:  
                return render(request, 'AllStudentsInfo.html',{'items':response.json(), "user":user})  
            except ValueError:
                print("Raw Response Content:", response.content.decode())
                return render(request, 'error.html',{ "info":'Invalid  response from Node.js'})  
        except Exception as e:
            return render(request, 'error.html',{ "info":f'Error during GET request: {str(e)}'}) 
    else:
        return render(request, 'LoginFail.html')
