import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'taskhub-secret-key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://taskhub_user:taskhub_pass@localhost:5432/taskhub_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key')
