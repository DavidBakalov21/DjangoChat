from django.shortcuts import render
def update_user(request,data, collection,first_email):
    try:
        search={'email':first_email}
        updated = {"$set": data}
        collection.update_one(search, updated)
        return render(request, 'UpdateSuccess.html')
    except Exception as e:
        return render(request, 'error.html',{ "info":f'Error: {str(e)}'}) 
    