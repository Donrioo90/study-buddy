from flask import Blueprint, request, jsonify
from .models import db, User
from flask_jwt_extended import create_access_token, jwt_required

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    # Authenticate user and return a JWT
    pass

@auth_routes.route('/register', methods=['POST'])
def register():
    # Register new user
    pass
