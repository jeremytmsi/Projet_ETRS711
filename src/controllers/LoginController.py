from flask_login import login_user, login_manager, current_user, login_required, logout_user

from app import app, db
from flask import render_template, url_for, redirect

from src.models.database.User import User
from src.models.forms.LoginForm import LoginForm
import hashlib

@app.route("/login",methods=["GET"])
def show_login_page():
    if current_user.is_authenticated:
        return redirect(url_for('show_profile_page'))
    form = LoginForm()
    return render_template('login.html',form=form)

@app.route("/login",methods=["POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = hashlib.sha1(str(form.password.data).encode()).hexdigest()

        try:
            user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one()
            if not user:
                raise Exception("User not found")
            else:
                if user.password == password:
                    login_user(user)
                    return redirect(url_for('show_profile_page'))
        except Exception:
                return render_template('login.html', error=True)


@app.login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('show_login_page'))