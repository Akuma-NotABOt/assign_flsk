from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    try:
        client = MongoClient(app.config['MONGO_URI'])
        app.db = client.get_default_database()
        app.db['users'].create_index('id', unique=True)
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise

    api = Api(app)
    from app.routes import initialize_routes
    initialize_routes(api)

    return app
