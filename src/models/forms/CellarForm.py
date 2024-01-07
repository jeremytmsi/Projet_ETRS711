from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CellarForm(FlaskForm):
    name = StringField("Nom de la cave", validators=[DataRequired()])
