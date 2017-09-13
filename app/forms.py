# forms.py

from app import app
from wtforms import Form, validators, StringField, SelectField, SubmitField
from wtforms.fields.html5 import IntegerRangeField


def get_choices(states):
    state_list = []
    for state in states:
        state_list.append((state,state))
    return state_list

class MeteoriteForm(Form):
    name = StringField('Name')
    mass = StringField('Mass')
    year = IntegerRangeField('Year', default=2012)
    submit = SubmitField('Submit')
