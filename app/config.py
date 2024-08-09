import os
import logging
from pythonjsonlogger import jsonlogger

def setup_logger():
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)

    logger = logging.getLogger('my-logger')
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)

    return logger

logger = setup_logger()
logger.info("Logger initialized", extra={"app": "User Management API", "version": "1.0.0"})

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/myDatabase')
