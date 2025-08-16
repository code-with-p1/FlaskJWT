import bcrypt

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Mock user database
users = [
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2')
]