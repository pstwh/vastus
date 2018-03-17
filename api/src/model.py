from src.database import database
from bson.objectid import ObjectId
from bson.json_util import dumps

class Model():
    def __init__(self, table_name):
        self.collection = database[table_name]
        
    def find(self, query):
        cursor = self.collection.find(query)
        return dumps(cursor)

    def find_one(self, query):
        cursor = self.collection.find_one(query)
        return dumps(cursor)

    def find_by_id(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def create(self, obj):
        return self.collection.insert_one(obj)

    def update(self, obj, id):
        pass

    def destroy(self, id):
        pass
        