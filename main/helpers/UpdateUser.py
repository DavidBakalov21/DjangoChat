from django.shortcuts import render
def update_user(request,data, collection,first_email):
    search={'email':first_email}
   
    updated = {"$set": data}
    collection.update_one(search, updated)
    return render(request, 'UpdateSuccess.html')
    