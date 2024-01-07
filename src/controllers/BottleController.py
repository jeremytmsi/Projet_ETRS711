from app import app,db

from flask import render_template, url_for, flash, redirect
from flask_login import login_required, current_user

from src.models.database.Bottle import Bottle
from src.models.forms.DeleteForm import DeleteForm


def get_bottle_by_id(id):
    return db.session.execute(db.select(Bottle).filter_by(id=id)).scalars().first()

@app.route("/profile/bottle/<id>")
def show_detailed_bottle(id):
    bottle = get_bottle_by_id(id)
    deleteForm = DeleteForm()
    return render_template("bottle.html",deleteForm = deleteForm, bottle=bottle)

@app.route("/profile/bottle/<id>/delete", methods=["POST"])
def delete_bottle(id):
    bottle = get_bottle_by_id(id)
    db.session.delete(bottle)
    db.session.commit()
    return redirect(url_for("get_detailed_shelf", id=bottle.shelf_id))