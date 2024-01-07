from sqlalchemy.exc import IntegrityError

from app import app,db
from flask import render_template, url_for, flash, redirect

from src.models.database.Bottle import Bottle
from src.models.database.Shelf import Shelf
from src.models.forms.BottleForm import BottleForm


def get_shelf_by_id(id):
    return db.session.execute(db.select(Shelf).filter_by(id=id)).scalars().first()


@app.route("/profile/shelf/<id>")
def get_detailed_shelf(id):
    shelf = get_shelf_by_id(id)
    bottles = get_bottles(id)
    form = BottleForm()
    return render_template("shelf.html", shelf=shelf, bottles=bottles, form=form)

@app.route("/profile/shelf/<id>/new_bottle", methods=["POST"])
def add_bottle(id):
    form = BottleForm()
    if form.validate_on_submit():
        bottle = Bottle(name=form.name.data, region=form.region.data, domain=form.domain.data, wine_type=form.wine_type.data, year=int(form.year.data), price=float(form.price.data), shelf_id=id, quantity=int(form.quantity.data))

        try:
            db.session.add(bottle)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Cette bouteille existe déjà")
        finally:
            return redirect(url_for("get_detailed_shelf", id=id))

def get_bottles(shelf_id):
    return db.session.execute(db.select(Bottle).filter_by(shelf_id=shelf_id)).scalars().all()