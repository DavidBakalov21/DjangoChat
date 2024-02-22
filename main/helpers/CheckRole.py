def check_role(collection,email):
    query = {"email":  email}
    document = collection.find_one(query)
    print(document)
    return document['selected_role']