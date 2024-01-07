from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app():
    db = SQLAlchemy()
    csrf = CSRFProtect()
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "projetM1"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://projet:projet@db:5432/projet_etrs711"
    csrf.init_app(app)
    Bootstrap(app)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    return app, db

app, db = create_app()
#login_manager = LoginManager()
#login_manager.init_app(app)

if __name__ == "__main__":
    app.run()

# Routes
import src.controllers.HomeController
import src.controllers.LoginController
import src.controllers.RegisterController
import src.controllers.ProfileController
import src.controllers.CellarController