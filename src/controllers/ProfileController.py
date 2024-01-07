from sqlalchemy.exc import IntegrityError

from app import app,db
from flask import render_template, url_for, flash, redirect
from flask_login import login_required, current_user

from src.models.database.Cellar import Cellar
from src.models.forms.CellarForm import CellarForm


@app.route("/profile")
@login_required
def show_profile_page():
    form = CellarForm()
    return render_template("profile.html",form=form)

@app.route("/profile/new_cellar", methods=["POST"])
def create_new_cellar():
    form = CellarForm()
    if form.validate_on_submit():
        cellar = Cellar(name=form.name.data, user_id=current_user.id)

        try:
            db.session.add(cellar)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Cette cave existe déjà")
        finally:
            return redirect(url_for("show_profile_page"))