from flask import Flask

app = Flask(__name__)

import src.controllers.HomeController

if __name__ == "__main__":
    app.run()