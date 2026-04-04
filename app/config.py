import os

class Config:
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    TESTING = os.environ.get('TESTING', 'False') == 'True'
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///default.db')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
    # Add more centralized settings as needed
