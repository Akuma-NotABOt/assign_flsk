from flask import Flask
from flask_restful import Api
import pymongo
from pymongo import MongoClient
from app.config import Config,logger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    try:
        client = MongoClient(app.config['MONGO_URI'])
        app.db = client.get_default_database()
        app.db['users'].create_index('id', unique=True)
        app.db['users'].create_index([('email', pymongo.ASCENDING)], unique=True)
        logger.info("Connected to MongoDB", extra={"MONGO_URI": Config.MONGO_URI})
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        raise

    api = Api(app)
    from app.routes import initialize_routes
    initialize_routes(api)

    return app
