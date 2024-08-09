from flask_restful import Resource, reqparse
from app.models import User
from flask import current_app as app
import pymongo.errors as err
from app.config import logger

class UserListResource(Resource):
    def get(self): #list all userdata in the database
        users = User(app.db).get_users()
        return users, 200

    def post(self): #input of new userdata
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        
        user_data = parser.parse_args()
        try:
            user_id = User(app.db).create_user(user_data)
            return {'id': str(user_id)}, 200
        except err.DuplicateKeyError:
            return {'message': 'User with this id or email already exists'}, 400
        except Exception as e:
            return {'message': "An error has occured when creating user"+str(e)}, 500 #for troubleshooting error

       #return {'id': user_id}, 200        

class UserResource(Resource):
    def get(self, user_id): #for getting a specific id
        user = User(app.db).get_user(user_id)
        if user:
            return user, 200
        return {'message': 'User not found'}, 404

    def put(self, user_id): #for editing data of speific user
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('email')
        parser.add_argument('password')
        data = parser.parse_args()
        User(app.db).update_user(user_id, data)
        return {'message': 'User data updated'}, 200

    def delete(self, user_id):#for deleting specific user 
        User(app.db).delete_user(user_id)
        return {'message': 'User data deleted'}, 200

def initialize_routes(api):
    logger.info("Initializing routes")
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<user_id>')
