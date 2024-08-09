from app import create_app
from app.config import logger

app = create_app()

if __name__ == '__main__':
    logger.info("Starting the Flask application")
    app.run(debug=True, host='0.0.0.0')
