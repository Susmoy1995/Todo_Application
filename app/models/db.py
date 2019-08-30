import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient('mongodb://localhost/27017')
mydb = myclient['todos']
mycol = mydb['lists']


def insert(data):
    x = mycol.insert_one(data)

    if x.inserted_id is not None:
        return True
    return False

def showListItem():
    return mycol.find()

def deleteItem(id):
    query = {'_id': ObjectId(id)}
    x = mycol.delete_one(query)
    print(x.deleted_count, 'document deleted')