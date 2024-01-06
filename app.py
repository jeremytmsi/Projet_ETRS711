from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


def create_app():
    db = SQLAlchemy()
    csrf = CSRFProtect()
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "projetM1"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://projet:projet@db:5432/projet_etrs711"
    csrf.init_app(app)
    Bootstrap(app)
    db.init_app(app)
    return app, db

app, db = create_app()

# Routes
import src.controllers.HomeController
import src.controllers.LoginController
import src.controllers.RegisterController

if __name__ == "__main__":
    app.run()