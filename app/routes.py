# routes.py

from app import app, models
from flask import render_template, redirect, request, url_for, json, jsonify
import requests

import os
from .models import *
from .queries import *
from .forms import *

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MeteoriteForm(request.form, csrf_enabled=True)
    year = form.year.data

    # --- POST ---
    # if request.method == 'POST':
    data = create_meteorite_dict(year)

    # --- GET ---
    content = { "form":form, "data":data }
    return render_template(
        'index.html',
        content=content,
         )
