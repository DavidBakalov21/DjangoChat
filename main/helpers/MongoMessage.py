from pymongo import MongoClient
import certifi
def get_mongo_message_collection():
    client = MongoClient('mongodb+srv://dbakalov:GW40QUxsOcyLzsY7@djangoapp.cpm7frk.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
    db = client['Chatbot']
    collection = db['RoomMessages']
    return collection