from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
# from backend.config import Config
from config import Config
from app.routes.auth import auth_bp
from app.routes.tasks import tasks_bp


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#     CORS(app)

#     from app.routes.auth import auth_bp
#     from app.routes.tasks import tasks_bp
#     app.register_blueprint(auth_bp, url_prefix="/api/auth")
#     app.register_blueprint(tasks_bp, url_prefix="/api/tasks")
#     app.register_blueprint(auth_bp, url_prefix="/auth")

#     return app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import auth_bp
  # ensure only imported once

    app.register_blueprint(auth_bp, url_prefix="/auth")  # register ONCE

    return app
