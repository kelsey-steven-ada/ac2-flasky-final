from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os 

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        app.config["Testing"] = True
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    from app.models.cat import Cat
    from app.models.caretaker import Caretaker

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.cat_routes import cats_bp
    app.register_blueprint(cats_bp)

    from .routes.caretaker_routes import caretakers_bp
    app.register_blueprint(caretakers_bp)

    return app