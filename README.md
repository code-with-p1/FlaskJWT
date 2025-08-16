# Flask JWT Authentication API

A robust Flask-based REST API demonstrating JSON Web Token (JWT) authentication with secure password hashing, environment variable configuration, and modular route handling.

## Features

- JWT-based authentication using Flask-JWT-Extended
- Secure password hashing with bcrypt
- Environment variable configuration with python-dotenv
- Cross-Origin Resource Sharing (CORS) support
- Modular route handling with Flask Blueprints
- Comprehensive logging
- Error handling for common HTTP errors

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   Create a `.env` file in the project root with the following content:
   ```env
   SECRET_KEY=your-secure-secret-key
   JWT_SECRET_KEY=your-secure-jwt-secret-key
   FLASK_DEBUG=True
   PORT=5000
   ```
   Replace `your-secure-secret-key` and `your-secure-jwt-secret-key` with strong, unique values.

## Running the Application

1. **Start the Flask App**:
   ```bash
   python app.py
   ```
   The application will run on `http://127.0.0.1:5000` (or the port specified in `.env`).

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

**Note**: Passwords are hashed using bcrypt. In production, use a secure database like PostgreSQL or MongoDB.

## Project Structure

```
your-repo-name/
├── app.py              # Main Flask application
├── .env                # Environment variables (not tracked in Git)
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore file
```

## Security Notes

- **Secret Keys**: Store `SECRET_KEY` and `JWT_SECRET_KEY` in `.env` and never commit them to Git.
- **Password Hashing**: Passwords are hashed using bcrypt for security.
- **CORS**: Configured to allow all origins (`*`) for demo purposes. Restrict origins in production.
- **Debug Mode**: Set `FLASK_DEBUG=False` in production.
- **HTTPS**: Use HTTPS in production to secure JWT tokens.

## Troubleshooting

- **Module Not Found**: Run `pip install -r requirements.txt`.
- **Invalid Token**: Ensure the `Authorization` header is formatted as `Bearer <token>`.
- **Port Conflict**: Change the `PORT` in `.env` or kill the process using the port.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.