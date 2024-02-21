def add_message(insert_data, collection):
    collection.insert_one({"message":insert_data[0], "room":insert_data[1]})
    