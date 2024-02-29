from django.shortcuts import render
def login_user(request,insert_data, collection):
    try:
        result=collection.find_one({"email":insert_data[0], "password":insert_data[1]})
        if result: 
            return render(request,'success.html', {'email':insert_data[0]})
        else:
            return render(request,'Loginfail.html')
    except Exception as e:
        print(e)
        #return render(request, 'error.html',{ "info":f'Error: {str(e)}'}) 