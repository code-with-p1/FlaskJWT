import os
import logging
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_cors import CORS
from flask import Blueprint
import bcrypt
from dotenv import load_dotenv
from http import HTTPStatus

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Load configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-default-secret-key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-default-jwt-secret-key')
app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Tokens in Authorization header

# Initialize extensions
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for demo purposes

# Define Blueprint for auth routes
auth_bp = Blueprint('auth', __name__)

# User class for data structure
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password  # Hashed password

# Mock user database (in production, use a proper database)
users = [
    User(1, 'user1', bcrypt.hashpw('password1'.encode('utf-8'), bcrypt.gensalt())),
    User(2, 'user2', bcrypt.hashpw('password2'.encode('utf-8'), bcrypt.gensalt())),
]

# Helper function to find user by username
def find_user_by_username(username):
    return next((user for user in users if user.username == username), None)

# Helper function to validate request data
def validate_login_data(data):
    if not data or 'username' not in data or 'password' not in data:
        return False, {"msg": "Missing username or password"}
    return True, None

# Root endpoint
@auth_bp.route('/', methods=['GET'])
def index():
    """Root endpoint to check if the API is running."""
    logger.info("Root endpoint accessed")
    return jsonify({"message": "Welcome to Flask JWT Authentication API"}), HTTPStatus.OK

# Login endpoint
@auth_bp.route('/login', methods=['POST'])
def login():
    """Authenticate user and return JWT access token."""
    logger.info("Login attempt initiated")
    
    # Validate request data
    is_valid, error = validate_login_data(request.json)
    if not is_valid:
        logger.warning("Invalid login data provided")
        return jsonify(error), HTTPStatus.BAD_REQUEST

    username = request.json.get('username')
    password = request.json.get('password').encode('utf-8')

    # Find user
    user = find_user_by_username(username)
    if not user:
        logger.warning(f"User not found: {username}")
        return jsonify({"msg": "Invalid username or password"}), HTTPStatus.UNAUTHORIZED

    # Verify password
    if not bcrypt.checkpw(password, user.password):
        logger.warning(f"Invalid password for user: {username}")
        return jsonify({"msg": "Invalid username or password"}), HTTPStatus.UNAUTHORIZED

    # Create and return access token
    access_token = create_access_token(identity=user.id)
    logger.info(f"Successful login for user: {username}")
    return jsonify({"access_token": access_token}), HTTPStatus.OK

# Protected endpoint
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """Access protected resource, requires valid JWT token."""
    current_user_id = get_jwt_identity()
    logger.info(f"Protected endpoint accessed by user ID: {current_user_id}")

    user = next((user for user in users if user.id == current_user_id), None)
    if not user:
        logger.warning(f"User not found for ID: {current_user_id}")
        return jsonify({"msg": "User not found"}), HTTPStatus.NOT_FOUND

    return jsonify({"logged_in_as": user.username}), HTTPStatus.OK

# Register Blueprint
app.register_blueprint(auth_bp)

# Error handlers
@app.errorhandler(HTTPStatus.NOT_FOUND)
def handle_404(error):
    logger.error(f"404 error: {str(error)}")
    return jsonify({"msg": "Resource not found"}), HTTPStatus.NOT_FOUND

@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def handle_500(error):
    logger.error(f"Server error: {str(error)}")
    return jsonify({"msg": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=os.getenv('FLASK_DEBUG', 'False') == 'True')