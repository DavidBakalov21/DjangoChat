from django.shortcuts import render
def display_user(request, collection,email):
    try:
        query = {"email":  email}
        document = collection.find_one(query)
        return render(request, 'UserProfile.html', {'item': document, 'email': email})
    except Exception as e:
        return render(request, 'error.html',{ "info":f'Error: {str(e)}'}) 