from app import app
from flask import render_template, url_for
from flask_login import login_required

@app.route("/profile")
@login_required
def show_profile_page():
    return render_template("profile.html")

@app.route("/profile/new_cellar")
def create_new_cellar():
    # TODO: implement the function to create a new cellar
    pass