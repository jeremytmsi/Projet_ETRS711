from app import app
from flask import render_template, url_for
from src.models.forms.RegisterForm import RegisterForm

@app.route("/register")
def show_register_page():
    form = RegisterForm()
    return render_template('register.html',form=form)