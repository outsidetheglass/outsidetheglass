# routes.py

from flask import render_template, redirect, request, url_for
from app import app
from .models import *
from .queries import *
from .forms import *

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StateForm(request.form, csrf_enabled=True)
    name, state = form.name.data, form.state.data

    print("name")
    print(name)
    print("state")
    print(state)
    # --- POST ---
    if request.method == 'POST':
        query = create_facility_dict(name, state)

    # --- GET ---
    content = {"form": form}
    return render_template('index.html', content=content)
