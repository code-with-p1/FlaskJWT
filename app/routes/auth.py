import logging
from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from http import HTTPStatus
from app.utils.helpers import find_user_by_username, validate_login_data
from app.models.user import users
import bcrypt
from flask import Blueprint

# Initialize logger
logger = logging.getLogger(__name__)

# Define Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET'])
def index():
    """Root endpoint to check if the API is running."""
    logger.info("Root endpoint accessed")
    return jsonify({"message": "Welcome to Flask JWT Authentication API"}), HTTPStatus.OK

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