from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired


class ShelfForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    bottles_per_shelf = StringField('Nombre de bouteilles par étagère', validators=[DataRequired()])
    region = StringField('Région', validators=[DataRequired()])