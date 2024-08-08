from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, db):
        self.db = db
        self.collection = self.db['users']

    def create_user(self, data):
        data['password'] = generate_password_hash(data['password'])
        try:
            result=self.collection.insert_one(data)
            return result.inserted_id
        except Exception as e:
            raise e
        
    def get_users(self):
        return list(self.collection.find({}, {'_id': 0}))

    def get_user(self, user_id):
        return self.collection.find_one({'id': user_id}, {'_id': 0})

    def update_user(self, user_id, data):
        if 'password' in data:
            data['password'] = generate_password_hash(data['password'])
        return self.collection.update_one({'id': user_id}, {'$set': data})

    def delete_user(self, user_id):
        return self.collection.delete_one({'id': user_id})
