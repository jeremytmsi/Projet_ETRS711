from app import app
from flask import render_template, url_for
from src.models.forms.LoginForm import LoginForm

@app.route("/login")
def show_login_page():
    form = LoginForm()
    return render_template('login.html',form=form)