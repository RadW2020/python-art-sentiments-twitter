from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

class UserNameForm(Form):
    name = StringField('Nombre:')
    name2 = StringField('Nombre:')
    name3 = StringField('Nombre:')
    name4 = StringField('Nombre:')
    submit = SubmitField('Generar respuesta')
