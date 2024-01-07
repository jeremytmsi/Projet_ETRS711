from sqlalchemy.exc import IntegrityError

from app import app,db
from flask import render_template, url_for, flash, redirect
from flask_login import login_required, current_user

from src.models.database.Cellar import Cellar
from src.models.database.Shelf import Shelf
from src.models.forms.ShelfForm import ShelfForm


def get_cellar_by_id(id):
    return db.session.execute(db.select(Cellar).filter_by(id=id)).scalars().first()


@app.route("/profile/cellar/<id>")
def get_detailed_cellar(id):
    cellar = get_cellar_by_id(id)
    shelfs = get_shelfs(id)
    form = ShelfForm()
    return render_template("cellar.html", cellar=cellar,shelfs=shelfs, form=form)

def get_shelfs(cellar_id):
    return db.session.execute(db.select(Shelf).filter_by(cellar_id=cellar_id)).scalars().all()

@app.route("/profile/cellar/<id>/new_shelf", methods=["POST"])
def create_shelf(id):
    form = ShelfForm()
    if form.validate_on_submit():
        shelf = Shelf(name=form.name.data, available_bottles=form.bottles_per_shelf.data, region=form.region.data, cellar_id=id)

        try:
            db.session.add(shelf)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Cette étagère existe déjà")
        finally:
            return redirect(url_for("get_detailed_cellar", id=id))
