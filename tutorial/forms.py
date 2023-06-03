from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FormularioDeNomes(FlaskForm):

    nome = StringField(label='Nome: ', validators=[DataRequired()])
    submit = SubmitField(label='Registrar')