from sqlalchemy.exc import IntegrityError

from app import app, db
from flask import render_template, url_for

import hashlib

from src.models.database.User import User
from src.models.forms.RegisterForm import RegisterForm

@app.route("/register",methods=["GET"])
def show_register_page():
    form = RegisterForm()
    return render_template('register.html',form=form)

@app.route("/register",methods=["POST"])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = hashlib.sha1(str(form.password.data).encode()).hexdigest()

        user = User(username,password)

        try:
            db.session.add(user)
            db.session.commit()
            success = True
            error = False
        except IntegrityError:
            error = True
            success = False
            db.session.rollback()

    return render_template("register.html",form=form,success=success,error=error)