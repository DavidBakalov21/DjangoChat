from django.shortcuts import render
from django.core.cache import cache
def update_user(request,data, collection,first_email):
    try:
        search={'email':first_email}
        updated = {"$set": data}
        collection.update_one(search, updated)
        cache.delete('user_profile_' + first_email)
        return render(request, 'UpdateSuccess.html', {'email':first_email})
    except Exception as e:
        print(e)
        #return render(request, 'error.html',{ "info":f'Error: {str(e)}'}) 
    