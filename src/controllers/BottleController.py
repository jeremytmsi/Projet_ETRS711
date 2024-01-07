from app import app,db

from flask import render_template, url_for, flash, redirect
from flask_login import login_required, current_user

from src.models.database.Bottle import Bottle

def get_bottle_by_id(id):
    return db.session.execute(db.select(Bottle).filter_by(id=id)).scalars().first()

@app.route("/profile/bottle/<id>")
def show_detailed_bottle(id):
    bottle = get_bottle_by_id(id)
    return render_template("bottle.html", bottle=bottle)