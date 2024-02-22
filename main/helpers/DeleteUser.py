def delete_user(collection,user):
    myquery = { "email": user }
    collection.delete_one(myquery)