from django.shortcuts import render
from django.core.cache import cache
def display_user(request, collection,email):
    try:
        document = cache.get('user_profile_'+email)
        if document is None:
            query = {"email":  email}
            document = collection.find_one(query)
            cache.set('user_profile_'+email, document,100)
        return render(request, 'UserProfile.html', {'item': document, 'email': email})
    except Exception as e:
        print(e)
        #return render(request, 'error.html',{ "info":f'Error: {str(e)}'}) 