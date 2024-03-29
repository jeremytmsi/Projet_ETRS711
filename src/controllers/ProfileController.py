from sqlalchemy.exc import IntegrityError

from app import app,db
from flask import render_template, url_for, flash, redirect
from flask_login import login_required, current_user

from src.models.database.Cellar import Cellar
from src.models.forms.CellarForm import CellarForm


'''
    Affiche la page de profil de l'utilisateur
'''
@app.route("/profile")
@login_required
def show_profile_page():
    form = CellarForm()
    cellars = get_user_cellars()
    return render_template("profile.html",form=form, cellars=cellars)

'''
    Permet de créer une cave
'''
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

'''
    Permet de récupèrer les caves de l'utilisateur
'''
def get_user_cellars():
    return db.session.execute(db.select(Cellar).filter_by(user_id=current_user.id)).scalars().all()