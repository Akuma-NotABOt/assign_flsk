from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from app.config import logger #for logging

class User:
    def __init__(self, db):#inititalize model
        self.db = db
        self.collection = self.db['users']
        logger.info("User model created")

    def create_user(self, data):
        data['password'] = generate_password_hash(data['password'])
        try:
            result=self.collection.insert_one(data)
            logger.info("User created", extra={"user_id": str(result.inserted_id)})
            return result.inserted_id
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise e
        
    def get_users(self):
        usr = list(self.collection.find({}, {'_id': 0}))
        logger.info("Retrieved all users", extra={"count": len(usr)})
        return usr
        

    def get_user(self, user_id):
        usr =  self.collection.find_one({'id': user_id}, {'_id': 0})
        if usr:
            logger.info("Retrieved user", extra={"user_id": user_id})
        else:
            logger.warning("User not found", extra={"user_id": user_id})
        return usr

    def update_user(self, user_id, data):
        if 'password' in data:
            data['password'] = generate_password_hash(data['password'])
        result = self.collection.update_one({'id': user_id}, {'$set': data})
        if result.matched_count > 0:
            logger.info("User updated", extra={"user_id": user_id})
        else:
            logger.warning("User not found for update", extra={"user_id": user_id})
        return result

    def delete_user(self, user_id):
        result = self.collection.delete_one({'id': user_id})
        if result.deleted_count > 0:
            logger.info("User deleted", extra={"user_id": user_id})
        else:
            logger.warning("User not found for deletion", extra={"user_id": user_id})
        return result