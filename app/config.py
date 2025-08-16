import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-default-jwt-secret-key')
    JWT_TOKEN_LOCATION = ['headers']