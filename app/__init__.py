from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate  # <-- Add this line
from .config import Config

db = SQLAlchemy()
migrate = Migrate()  # <-- Add this line
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)  # <-- Add this line
    jwt.init_app(app)

    from .routes import main_routes
    from .auth import auth_routes
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)

    return app
