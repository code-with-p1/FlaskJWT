# Flask JWT Authentication API

A modular Flask-based REST API demonstrating JSON Web Token (JWT) authentication with secure password hashing, environment variable configuration, and Flask Blueprints for scalability.

## Features

- JWT-based authentication using Flask-JWT-Extended
- Secure password hashing with bcrypt
- Environment variable configuration with python-dotenv
- Cross-Origin Resource Sharing (CORS) support
- Modular structure with Flask Blueprints
- Comprehensive logging
- Error handling for common HTTP errors

## Project Structure

```
FlaskJWT/
├── app/
│   ├── __init__.py        # Initializes Flask app and extensions
│   ├── config.py          # Configuration settings
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py        # User model
│   ├── routes/
│   │   ├── __init__.py
│   │   └── auth.py        # Authentication routes
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py     # Helper functions
├── .env                   # Environment variables (not tracked)
├── .env.example           # Example environment file
├── .gitignore             # Git ignore file
├── requirements.txt       # Dependencies
├── README.md              # This file
└── run.py                 # Entry point
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Generate secure keys:
     ```bash
     openssl rand -hex 32
     ```
   - Update `.env` with the generated keys:
     ```
     SECRET_KEY=<your-secure-key>
     JWT_SECRET_KEY=<your-secure-jwt-key>
     FLASK_DEBUG=True
     PORT=5000
     ```

## Running the Application

1. **Start the Flask App**:
   ```bash
   python run.py
   ```
   The app runs on `http://127.0.0.1:5000` (or the port specified in `.env`).

## API Endpoints

### 1. Root Endpoint (`/`)
- **Method**: GET
- **Description**: Returns a welcome message.
- **Example**:
  ```bash
  curl http://127.0.0.1:5000/
  ```
- **Response** (200):
  ```json
  {"message": "Welcome to Flask JWT Authentication API"}
  ```

### 2. Login Endpoint (`/login`)
- **Method**: POST
- **Description**: Authenticates a user and returns a JWT access token.
- **Request Body**:
  ```json
  {
      "username": "user1",
      "password": "password1"
  }
  ```
- **Example**:
  ```bash
  curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username":"user1","password":"password1"}'
  ```
- **Success Response** (200):
  ```json
  {"access_token": "<your-jwt-token>"}
  ```
- **Error Responses**:
  - 400: `{"msg": "Missing username or password"}`
  - 401: `{"msg": "Invalid username or password"}`

### 3. Protected Endpoint (`/protected`)
- **Method**: GET
- **Description**: Returns the username of the authenticated user. Requires a valid JWT token.
- **Headers**:
  - `Authorization: Bearer <your-jwt-token>`
- **Example**:
  ```bash
  curl -H "Authorization: Bearer <your-jwt-token>" http://127.0.0.1:5000/protected
  ```
- **Success Response** (200):
  ```json
  {"logged_in_as": "user1"}
  ```
- **Error Responses**:
  - 401: Invalid or missing token
  - 404: `{"msg": "User not found"}`

## Mock User Database

For demonstration, the app uses an in-memory user database:
- User 1: `username: user1`, `password: password1`
- User 2: `username: user2`, `password: password2`

**Note**: Passwords are hashed using bcrypt. In production, use a secure database.

## Security Notes

- **Secret Keys**: Store in `.env` and never commit to Git.
- **Password Hashing**: Uses bcrypt for secure password storage.
- **CORS**: Allows all origins (`*`) for demo. Restrict in production.
- **Debug Mode**: Set `FLASK_DEBUG=False` in production.
- **HTTPS**: Use HTTPS in production to secure JWT tokens.

## Troubleshooting

- **Module Not Found**: Run `pip install -r requirements.txt`.
- **Invalid Token**: Ensure `Authorization` header is `Bearer <token>`.
- **Port Conflict**: Change `PORT` in `.env` or free the port.

## Contributing

Contributions are welcome! Open an issue or submit a pull request.

## License

This project is licensed under the MIT License.