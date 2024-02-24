def add_message(insert_data, collection):
    try:
        collection.insert_one({"message":insert_data[0], "room":insert_data[1]})
    except Exception as e:
        print("troubles happened on server side")
    