from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes.route import my_bp
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(my_bp)

    return app
