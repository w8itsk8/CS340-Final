# Example Python Code to Insert a Document 
# Edited 3/30/2026 by Kate Wheeler for Module 4

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    # Connection Variables 
    # 
    USER = 'aacuser'
    PASS = 'password'
    HOST = 'localhost' 
    PORT = 27017 
    DB = 'aac' 
    COL = 'animals' 
    
    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections. This is hard-wired to use the aac  database, the animals collection, and the aac user. 
        
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (self.USER, self.PASS, self.HOST, self.PORT)) 
        self.database = self.client['%s' % (self.DB)] 
        self.collection = self.database['%s' % (self.COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            exists = self.collection.insert_one(data)  # data should be dictionary 
            if exists.acknowledged:
                return True
            else:
                return False
        else: 
            raise Exception("Nothing to save, because data parameter returned no records") 
            return []

    # Method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            result_list = list(self.collection.find(data))
            if len(result_list) == 0:
                return (f"Nothing here by those parameters.")
            else:
                return result_list
        else:
            raise Exception("Nothing to view, because data parameter returned no records")
            return []
        
    # Method to implement the U in CRUD
    def update(self, data, updated):
        if data is not None:
            counter = 0
            for item in self.collection.find(data):
                counter = counter + 1
            self.collection.update_many(data, updated)
            return counter
        else:
            raise Exception("Nothing to update, because data parameter returned no records")
            return []
    
    # Method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            counter = 0
            for item in self.collection.find(data):
                counter = counter + 1
            self.collection.delete_many(data)
            return counter
        else:
            raise Exception("Nothing to delete, because data parameter returned no records")
            return []
        
        
            