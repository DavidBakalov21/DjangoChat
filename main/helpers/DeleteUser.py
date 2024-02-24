def delete_user(collection,user):
    try:
        myquery = { "email": user }
        collection.delete_one(myquery)
    except Exception as e:
        print("error deleting user")