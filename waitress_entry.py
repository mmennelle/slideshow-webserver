import logging
from waitress import serve
from webserver import app

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('waitress')
    
    logger.info("Starting Waitress server on http://127.0.0.1:5000")
    
    # Run the application with Waitress
    serve(app, host='127.0.0.1', port=5000, _quiet=False)
