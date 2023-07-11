from flask_wtf import Form
from wtforms import StringField, SubmitField


class NameForm(Form):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')
