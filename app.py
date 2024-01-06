from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect


def create_app():
    csrf = CSRFProtect()
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "projetM1"
    csrf.init_app(app)
    Bootstrap(app)
    return app

app = create_app()

# Routes
import src.controllers.HomeController
import src.controllers.LoginController
import src.controllers.RegisterController

if __name__ == "__main__":
    app.run()