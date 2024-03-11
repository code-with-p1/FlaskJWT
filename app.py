from flask import Flask, jsonify
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = [
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2')
]

def authenticate(username, password):
    user = next((user for user in users if user.username == username and user.password == password), None)
    if user:
        return user

def identity(payload):
    user_id = payload['identity']
    return next((user for user in users if user.id == user_id), None)

def custom_auth_response_handler(access_token, identity):
    return jsonify({'access_token': access_token})

jwt = JWT(app, authenticate, identity)
jwt.auth_response_callback = custom_auth_response_handler


@app.route('/protected')
@jwt_required()
def protected():
    return jsonify(logged_in_as=current_identity.username), 200

if __name__ == '__main__':
    app.run(debug=True)
