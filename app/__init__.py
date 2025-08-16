import logging
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.config import Config
from app.routes.auth import auth_bp

# Initialize logger
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Initialize extensions
    JWTManager(app)
    CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for demo
    
    # Register Blueprints
    app.register_blueprint(auth_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def handle_404(error):
        logger.error(f"404 error: {str(error)}")
        return {"msg": "Resource not found"}, 404
    
    @app.errorhandler(500)
    def handle_500(error):
        logger.error(f"Server error: {str(error)}")
        return {"msg": "Internal server error"}, 500
    
    return app