from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development"

    from app.models.cat import Cat

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.cat_routes import cats_bp
    app.register_blueprint(cats_bp)

    return app