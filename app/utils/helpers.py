from app.models.user import users

def find_user_by_username(username):
    """Find a user by username in the mock database."""
    return next((user for user in users if user.username == username), None)

def validate_login_data(data):
    """Validate login request data."""
    if not data or 'username' not in data or 'password' not in data:
        return False, {"msg": "Missing username or password"}
    return True, None