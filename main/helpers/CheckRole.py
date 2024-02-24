def check_role(collection,email):
    try:
        query = {"email":  email}
        document = collection.find_one(query)
        print(document)
        if document is not None and 'selected_role' in document:
            return document['selected_role']
        else:
            return "not found"
    except Exception as e:
        return "not found"
    