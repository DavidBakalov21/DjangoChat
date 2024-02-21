def get_all_room_messages(collection,user1,user2):
    cleaned_user1 = user1.replace('@', '1').replace('.', '1')
    cleaned_user2 = user2.replace('@', '1').replace('.', '1')
    room_name=''.join(sorted([cleaned_user1, cleaned_user2]))
    query = {"room": room_name}
    documents = collection.find(query)
    documents_list = [doc for doc in documents]
    return documents_list
