from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.fields.numeric import FloatField, IntegerField
from wtforms.fields.simple import StringField, FileField
from wtforms.validators import DataRequired


class BottleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    domain = StringField('Domaine', validators=[DataRequired()])
    region = StringField('Region', validators=[DataRequired()])
    wine_type = StringField('Type de vin', validators=[DataRequired()])
    year = IntegerField('Année de la bouteille', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])