from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from libs.postgres.db import db

def create_app():
    """Factory function to create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # Initialize Flask-Migrate to handle Alembic migrations
    Migrate(app, db)

    with app.app_context():
        # Import routes to register them with the app
        from app.routes import bp
        app.register_blueprint(bp)

    return app
