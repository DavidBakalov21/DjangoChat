from django.shortcuts import render
def login_user(request,insert_data, collection):
    result=collection.find_one({"email":insert_data[0], "password":insert_data[1]})
    if result: 
        return render(request,'success.html')
    else:
        return render(request,'Loginfail.html')