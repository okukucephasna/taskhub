# backend/app/routes/__init__.py

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/hello')
def hello():
    return "Hello from auth!"
