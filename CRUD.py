
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId


# Initializing the MongoClient. This helps to 
    # access the MongoDB databases and collections.
    # This is hard-wired to use the aac database, the 
    # animals collection, and the aac user.
    # Definitions of the connection string variables are
    # unique to the individual Apporto environment.

class AnimalShelter(object):
    def __init__(self):
        USER = 'aacuser'
        PASS = 'MLP2002'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32423
        DB = 'AAC'
        COL = 'animals'
        
        #
        # Initialize Connection
        #
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    # Method to implement the C in CRUD.
    def create(self, data):
        
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary    
            return True        
        else:
            return False
            
    # Method to implement the R in CRUD.
    def read(self, query):
       
         try:
            results = list(self.collection.find(query))
            return results

         except Exception as e:
            print(f"Error reading data: {e}")
            return []

    # Method to implement the U in CRUD.
    def update(self, query, document):
        
        try:
            finalUpdate = self.database.animals.update_many(query, {"$set": document})
            return finalUpdate.modified_count
        
        except Exception as e:
            print(f"Error updating data: {e}")
            return []
        
    # Method to implement the D in CRUD.
    def delete(self, query):

        try:
            deleteResult = self.database.animals.delete_many(query)
            return deleteResult.deleted_count
        except Exception as e:
            print(f"Error deleting data: {e}")
            return []
