from flask_restful import Resource, reqparse
from app.models import User
from flask import current_app as app
import pymongo.errors as err

class UserListResource(Resource):
    def get(self):
        users = User(app.db).get_users()
        return users, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        
        data = parser.parse_args()
        try:
            user_id = User(app.db).create_user(data)
            return {'id': str(user_id)}, 200
        except err.DuplicateKeyError:
            return {'message': 'User with this id already exists'}, 400
        except Exception as e:
            return {'message': str(e)}, 500

        return {'id': user_id}, 200

class UserResource(Resource):
    def get(self, user_id):
        user = User(app.db).get_user(user_id)
        if user:
            return user, 200
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('email')
        parser.add_argument('password')
        data = parser.parse_args()
        User(app.db).update_user(user_id, data)
        return {'message': 'User updated'}, 200

    def delete(self, user_id):
        User(app.db).delete_user(user_id)
        return {'message': 'User deleted'}, 200

def initialize_routes(api):
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<user_id>')
