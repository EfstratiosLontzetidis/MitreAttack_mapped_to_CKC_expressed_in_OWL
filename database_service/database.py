from pymongo import MongoClient


class ClientDB:
    def __init__(self):
        pass

    client = MongoClient("mongodb://localhost:27017/")
    db = client["attackOWL"]
