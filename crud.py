from pymongo import MongoClient

class AnimalShelter:
    def __init__(self, username="aacuser", password="1234"):
        # MongoDB connection with hardcoded username and password
        self.client = MongoClient(f'mongodb://{username}:{password}@nv-desktop-services.apporto.com:32475/?authSource=admin')
        self.db = self.client['AAC']  # Access the AAC database
        self.collection = self.db['animals']  # Access the animals collection

    # Create method: Insert a document into the collection
    def create(self, data):
        if data:
            result = self.collection.insert_one(data)
            return result.acknowledged  # Returns True if successful, False otherwise
        else:
            raise Exception("No data to insert")

    # Read method: Find documents based on a query (filter)
    def read(self, query):
        return list(self.collection.find(query))  # Returns a list of documents

    # Update method: Modify documents that match the query
    def update(self, query, update_data):
        result = self.collection.update_many(query, {'$set': update_data})
        return result.modified_count  # Returns the number of modified documents

    # Delete method: Remove documents that match the query
    def delete(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count  # Returns the number of deleted documents
