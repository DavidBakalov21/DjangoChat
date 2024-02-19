from django.shortcuts import render
def display_user(request, collection,email):
    query = {"email":  email}
    document = collection.find_one(query)
    return render(request, 'UserProfile.html', {'item': document, 'email': email})