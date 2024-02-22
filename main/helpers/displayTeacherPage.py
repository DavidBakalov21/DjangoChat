from django.shortcuts import render
def display_all_teacher(request, collection,email):
    query = {"email": {"$ne": email}}
    documents = collection.find(query)
    documents_list = [doc for doc in documents]
    return render(request, 'chatListTeacher.html', {'items': documents_list, 'email':email})