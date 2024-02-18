from django.shortcuts import render
def display_all(request, collection,email):
    query = {"email": {"$ne": email}}
    documents = collection.find(query)
    documents_list = [doc for doc in documents]
    return render(request, 'chatList.html', {'items': documents_list, 'email':email})