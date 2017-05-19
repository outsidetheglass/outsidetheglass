# forms.py

from app import app
from wtforms import Form, validators, StringField, SelectField, SubmitField

states = ['', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

def get_choices(states):
    state_list = []
    for state in states:
        state_list.append((state,state))
    return state_list

class StateForm(Form):
    name = StringField('Campsite Facility')
    state = SelectField(choices=get_choices(states))
    submit = SubmitField('Submit')
